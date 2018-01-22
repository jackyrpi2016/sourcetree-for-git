# use regular expression to find phone number
import re
message = 'Call me 415-555-1101 tomorrow, or at 415-555-9999.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # use raw string, \d indicates number
mo = phoneNumRegex.findall(message)
print(mo)

# if search only one, use .search()
mo = phoneNumRegex.search(message)
print(mo.group())
