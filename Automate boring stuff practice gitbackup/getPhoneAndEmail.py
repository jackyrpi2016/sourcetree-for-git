# get phone number and email address from a large chunk of text

import re, pyperclip

# create a regex for phone numbers
# use verbose mode
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000 ext 12345, ext. 12345, x12345
# make sure to include those in a large group, when use findall()
(
((\d\d\d)|(\(\d\d\d\)))?            # area code (optional); only nums, empty, nums with ()
(\s|-)            # first separator; whitespace, -
\d\d\d            # first 3 digits
-            # second separator
\d\d\d\d            # last 4 digits
(((ext(\.)?\s)|x)            # extension word-part (optional), ext , ext. , x
(\d{2,5}))?            # extension number-part (optional), 2 to 5 digits
)
''', re.VERBOSE)

# create a regex for email address
emailRegex = re.compile(r'''
# some.+_thing@some.+_thing.com

[a-zA-Z0-9_.+]+        # name part
@        # @ symbol
[a-zA-Z0-9_.+]+        # domain name part

''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

# we set groups for phone number, so it return a list of tuples strings
allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Copy the extracted email/phone to the clipboard, remove ',' and '...'
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
