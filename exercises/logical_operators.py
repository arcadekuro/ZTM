""" Creating a game to test understanding of logical operators. """

is_magician = True
is_expert = True

# Check if magician AND exper: "You are a master magician"
if is_magician and is_expert:
    print("You are a master magician")
# Check if magician but no expert: "at least you're getting there"
elif is_magician and not is_expert:
    print("At least you're getting there")
# if your're not a magician: "You need magic powers"
elif not is_magician:
    print("You need magic powers")
