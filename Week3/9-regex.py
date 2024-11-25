# To implement Regular Expressions in Python, we use "re"

import re

# Prompting user for an email... but they can truly enter whatever they want.
user_email = input("What is your E-mail address? ")

# We need to check to make sure that they're entering a valid email in that string
email_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+"

# Now that we have our regex pattern to match against, we use some conditional logic to 
# check for pattern adherence

if re.match(email_regex, user_email):
    print("Email address is valid, thank you!")
else:
    print("You had one job, enter a valid email address :c")
