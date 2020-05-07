import time

"""
Understand what Epoch is.
Manage the concept of time using a float.
Float represents the number of seconds
that have passed since a time period began.
Considering a period of time defined by a starting point i.e an era.
In computing this is called an epoch!
"""


# The epoch is the starting point to measure passage of time
# Epoch on most os is 00:00january 1st 1970 UTC
# Epoch time is the number of seconds that have passed since then.
# this has no meaning to us.


def local_time():
    epc = time.time()
    localtime = time.localtime(epc)
    print(localtime)  # ouput nor specific to format.
    print(time.ctime(epc))


local_time()
