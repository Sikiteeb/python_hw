# Sigrid Hanni
# huge help from regex101.com and
# https://www.w3resource.com/javascript/form/email-validation.php

import re

# open and read the input file
with open("valid_input.txt", "r") as file:
    lines = file.readlines()

# remove all before colon and colon from each line to target the value
# not the beginning of the line, with split and strip

# validate first name and last name
if not re.match(r"^[A-Z][a-z]+\s[A-Z][a-z]+$", lines[0].split(":")[1].strip()):
    print("Line 1 contains invalid values")

# validate email address
if not re.match(r"^(?!\.)(?!.*\.$)(?!.*\.\.)[a-zA-Z0-9._%+-]+@(?!-)(?!-*-$)(?!.*-)(?!\d)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
                lines[1].split(":")[1].strip()):
    print("Line 2 contains invalid values")

# validate age
if not re.match(r"^\d+$", lines[2].split(":")[1].strip()):
    print("Line 3 contains invalid values")

# validate favourite website
if not re.match(r"^www\.\S+$", lines[3].split(":")[1].strip()):
    print("Line 4 contains invalid values")

# validate business time
if not re.match(r"^[01]\d|2[0-3]:[0-5]\d-(?:[01]\d|2[0-3]):[0-5][0-5]\d$", lines[4].split(":")[1].strip()):
    print("Line 5 contains invalid values")

# if all fields are valid, print "All fields are valid"
if all([re.match(r"^[A-Z][a-z]+\s[A-Z][a-z]+$", lines[0].split(":")[1].strip()),
        re.match(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$",
                 lines[1].split(":")[1].strip()),
        re.match(r"^\d+$", lines[2].split(":")[1].strip()),
        re.match(r"^www\.\S+$", lines[3].split(":")[1].strip()),
        re.match(r"^[01]\d|2[0-3]:[0-5]\d-(?:[01]\d|2[0-3]):[0-5]\d$", lines[4].split(":")[1].strip())]):
    print("All fields are valid")
