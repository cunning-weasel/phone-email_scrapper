import re, pyperclip

# Create Regex Object for phone numbers
phoneRegex = re.compile(r'''
# Types of phone numbers: 415-555-0000, 555-0000, (415) 555-0000 ext 12345, ext. 12345, x12345

((\d\d\d)|(\(\d\d\d\d\)))?      # area code (optional)
(\s|-)                          # first separator
\d\d\d                          # first 3 digits
-                               # separator
\d\d\d\d                        # last 4 digits
(((ext(\.)?\s)|x)               # extension word-part (optional)
(\d{2,5}))?                     # extnesion number-part (optional) + syntax means the digit could appear 2 or more times
''', re.VERBOSE)                # re.VERBOSE as second argument to compile function
                                # let's me multi-line + triple colon my string + comment in-string

# Create Regex Object for email addresses
emailRegex = re.compile(r'''
                                # some.+_thing @ (\d{2,5}))?  .com

[a-zA-Z0-9_.+]+                 # name part
@                               # @ symbol
[a-zA-Z0-9_.+]+                 # domain name part

''', re.VERBOSE)

# Get the text off the clipboard. pyperclip module works just with ctrl+c ! weeeeeeeee
text = pyperclip.paste()

# Extract the email/ phone numbers from this text
extractedPhone = phoneRegex.findall(text)           # findall method returns list of strings
extractedEmail = emailRegex.findall(text)

allPhoneNumbers =[]
for phoneNumber in extractedPhone:                  # each iteration through the loop, phoneNumber variable is assigned a
    allPhoneNumbers.append(phoneNumber[0])          # single tuple from extractedPhone variable

# Copy the extracted email/phone to the clipboard, hella pretty
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail) # join takes a list of strings and joins them into single string
pyperclip.copy(results)

