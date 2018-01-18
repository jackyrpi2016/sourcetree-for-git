>>> # find and replace
>>> import re
>>> namesRegex = re.compile(r'Agent \w+')
>>> namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')
['Agent Alice', 'Agent Bob']
>>> # use sub() to encode the info
>>> namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.')
'REDACTED gave the secret documents to REDACTED.'
>>> 
>>> # show the first character but encode the rest
>>> namesRegex = re.compile(r'Agent (\w)\w*')  # group the first character and include the rest
>>> namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')
['A', 'B']
>>> # there is only one group 'A' and 'B', use () to identify the characte we want
>>> namesRegex = re.compile(r'Agent \w')
>>> namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')
['Agent A', 'Agent B']
>>> 
>>> namesRegex = re.compile(r'Agent (\w)\w*')  # group the first character and include the rest
>>> namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.')
'Agent A**** gave the secret documents to Agent B****.'
>>> # group 1 and add ****
>>> 
>>> 
>>> 
>>> 
>>> # phone number example
>>> re.compile(r'\(\d\d\d\)(-)?\d\d\d-\d\d\d\d')  # get puzzled, the next time to see
re.compile('\\(\\d\\d\\d\\)(-)?\\d\\d\\d-\\d\\d\\d\\d')
>>> # use verbose mode
>>> re.compile(r'''
(\d\d\d-)|    # area code (without parens, with dash)
(\(\d\d\d\) )  # -or- area code with parens and no dash
\d\d\d         # first 3 digits
-               # second dash
\d\d\d\d        # last 4 digits
\sx\d{2,4}     # extension, like x1234''', re.VERBOSE)
re.compile('\n(\\d\\d\\d-)|    # area code (without parens, with dash)\n(\\(\\d\\d\\d\\) )  # -or- area code with parens and no dash\n\\d\\d\\d         # first 3 digits\n-               # second dash\n\\d\\d\\d\, re.VERBOSE)
>>> print(re.compile(r'''
(\d\d\d-)|    # area code (without parens, with dash)
(\(\d\d\d\) )  # -or- area code with parens and no dash
\d\d\d         # first 3 digits
-               # second dash
\d\d\d\d        # last 4 digits
\sx\d{2,4}     # extension, like x1234''', re.VERBOSE))
re.compile('\n(\\d\\d\\d-)|    # area code (without parens, with dash)\n(\\(\\d\\d\\d\\) )  # -or- area code with parens and no dash\n\\d\\d\\d         # first 3 digits\n-               # second dash\n\\d\\d\\d\, re.VERBOSE)
>>> # use multiple choices for second parameter, use |
>>> re.compile(..., re.IGNORECASE | re.DOTALL | re.VERBOSE)
