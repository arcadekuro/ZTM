"""
Compiles a segment conversion report for the given date range.
Retrieves Brand, segment, device, geo and external order ID.
Emails a csv with the resulting rows to `EMAIL_RECIPIENTS`.
"""

import pandas as pd

from custom_reports.utils import (
    presto as presto_utils,
    email as email_utils,
    log as log_utils,
)

logger = log_utils.get_logger(__name__)

FILE_PATH = "/tmp/"
FILE_PREFIX = "Golf_brand_conversion_report"

ACCOUNT_ID = '5c055e35053a1bf609aaf5ee'
BRAND_ID = "5cde821cae122c1f00f818d2"
SEGMENT_ID = "5cde8333ae122c1f00f818d6"

EMAIL_SUBJECT = "Brand level Media Drive Conversion report"
EMAIL_RECIPIENTS = [
    "fernando@avocet.io",
    "arcade@avocet.io"
]


def query_conversion_logs(table_name, start_date, end_date):

    query = "SELECT timestamp, brand_id, segment_id, attribution_mode, device_type, request_domain, country, country_subdivision, city, SUM (advertiser_revenue_value) AS order_revenue, external_order_id FROM {} WHERE timestamp_trunc_hour >= DATE_FORMAT(timestamp '{} 00:00:00 UTC' AT TIME ZONE 'UTC', '%Y-%m-%d-%H') AND timestamp_trunc_hour <= DATE_FORMAT(timestamp '{} 23:59:59 UTC' AT TIME ZONE 'UTC', '%Y-%m-%d-%H') AND timestamp_trunc_hour >= DATE_FORMAT(timestamp '{} 00:00:00 UTC' AT TIME ZONE 'UTC', '%Y-%m-%d-%H') AND timestamp_trunc_hour <= DATE_FORMAT(timestamp '{} 23:59:59 UTC' AT TIME ZONE 'UTC', '%Y-%m-%d-%H') AND (account_id = '{}') AND (brand_id = '{}') AND (segment_id = '{}') AND (COALESCE(attribution_mode, 0) = 0) GROUP BY 1, 2, 3, 4, 5, 6, 7, 8, 9, 11 ORDER BY 1 ASC".format(table_name, start_date, end_date, start_date, end_date, ACCOUNT_ID, BRAND_ID, SEGMENT_ID)

    headers = ['Timestamp', 'Brand', 'Segment ID', 'Attribution mode', 'Device', 'Request Domain', 'Country', 'Country Subdivision', 'City', 'Order Revenue', 'Order ID']

    logger.info("Running query on table '%s'", table_name)
    logger.debug("Query '%s'", query)

    return presto_utils.run_query(query, headers)


def combine_conversion_logs_data(start_date, end_date):
    postview = query_conversion_logs(
        'postviewconversion_logs',
        start_date,
        end_date
    )

    postviewable = query_conversion_logs(
        'postviewableconversion_logs',
        start_date,
        end_date
    )

    postclick = query_conversion_logs(
        'postclickconversion_logs',
        start_date,
        end_date
    )

    logger.debug("Results sample 'postview': %s", postview.head())
    logger.debug("Results sample 'postviewable': %s", postviewable.head())
    logger.debug("Results sample 'postclick': %s", postclick.head())
    logger.info("Mapping 'Total_Conversions', 'PV', 'VPV' and 'PC' to results")

    postview.assign(**{'Total_Conversions': 1, 'PV': 1, 'VPV': 0, 'PC': 0})

    postviewable.assign(**{'Total Conversions': 1, 'PV': 1, 'VPV': 1, 'PC': 0})

    postclick.assign(**{'Total Conversions': 1, 'PV': 0, 'VPV': 0, 'PC': 1})

    logger.info("Results sample after mapping:")
    logger.debug("'postview': %s", postview.head())
    logger.debug("'postviewable': %s", postviewable.head())
    logger.debug("'postclick': %s", postclick.head())

    logger.debug("Concatenating query results")

    return pd.concat(
        [postview, postviewable, postclick], axis=0,
        ignore_index=True
    )


def run(destination_path, start_date, end_date):
    data_frame = combine_conversion_logs_data(start_date, end_date)

    logger.info(
        "Query executed successfully with %s results",
        data_frame.shape[0]
    )

    logger.debug("%s", data_frame.head())

    logger.info("Exporting query results to csv file '%s'", destination_path)
    data_frame.to_csv(destination_path, index=False)

    return destination_path


def main():
    start_date = "2019-09-12"
    end_date = "2019-12-31"

    file_name = "{}_{}.csv".format(FILE_PREFIX, end_date)
    file_path = "{}{}".format(FILE_PATH, file_name)

    destination = run(
        file_path,
        start_date,
        end_date
    )

    rendered_subject = "{} {}".format(
        EMAIL_SUBJECT,
        end_date
    )

    logger.info(
        "Emailing report to %s with subject '%s'",
        EMAIL_RECIPIENTS,
        rendered_subject
    )

    email_utils.send_report(
        rendered_subject,
        EMAIL_RECIPIENTS,
        destination
    )

    logger.info("Report completed and sent successfully")


if __name__ == '__main__':
    main()