#! /usr/bin/env python3

import re, pyperclip

#  - create regx object for phone numbers
phoneRegex = re.compile(r''' 
# 415-555-000, 555-000, (415) 555-000, 555-000 ext 12345, ext. 12345, x12345
(
((\d\d\d) | (\(\d\d\d\)))?   # area code (optional)
(\s|-)                       # first seperator
\d\d\d                       # first three digits
-                            # seperator
\d\d\d\d                     # last four digits
((ext(\.)?\s) | x)           # extension word-part (optional)
(\d(2,5))?                    # extension number-part (optional)
)

''', re.VERBOSE)

#  - create regx object for emails

emailRegex = re.compile(r'''
# some.+_thing@something.com

[a-zA_Z0-9_.+]+     # name part
@                   # @ symbol (universal)
[a-zA_Z0-9_.+]+     # domain name

 ''')

# todo - get the text off the clipboard

text = pyperclip.paste()

# todo - extract the emails and phone numbers from the text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

print(extractedEmail)
print(extractedPhone)
print(allPhoneNumbers)

# todo - copy the extracted info to clipboard

results = '\n'.join(allPhoneNumbers) +'\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
print(results)
