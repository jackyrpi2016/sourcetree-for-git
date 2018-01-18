>>> import re
>>> # ^, start with ...
>>> beginsWithHelloRegex = re.compile(r'^Hello')
>>> beginsWithHelloRegex.search('Hello there!')
<_sre.SRE_Match object; span=(0, 5), match='Hello'>
>>> beginsWithHelloRegex.search('He said "Hello!"')
>>> beginsWithHelloRegex.search('He said "Hello!"') == None
True
>>> 
>>> # $, ends with ...
>>> endsWithWorldRegex = re.compile(r'world!$')
>>> endsWithWorldRegex.search('Hello world!')
<_sre.SRE_Match object; span=(6, 12), match='world!'>
>>> endsWithWorldRegex.search('Hello world!shosdhifosdfhi')
>>> endsWithWorldRegex.search('Hello world!shosdhifosdfhi') == None
True
>>> 
>>> # ^...$, must be exact ...
>>> allDigitsRegex = re.compile(r'^\d+$')
>>> allDigitsRegex.search('314214214243432')
<_sre.SRE_Match object; span=(0, 15), match='314214214243432'>
>>> allDigitsRegex.search('314214214d243432')
>>> allDigitsRegex.search('314214214d243432') == None
True
>>> 
>>> # ., anything but new line
>>> atRegex = re.compile(r'.at')
>>> atRegex.findall('the cat in the hat sat on the flat mat.')
['cat', 'hat', 'sat', 'lat', 'mat']
>>> # .at means select only on character, so flat is not in
>>> 
>>> # select 1 or 2
>>> atRegex = re.compile(r'.{1,2}at')
>>> atRegex.findall('the cat in the hat sat on the flat mat.')
[' cat', ' hat', ' sat', 'flat', ' mat']
>>> # we get flat this time, but notice the white space before cat and ....
>>> 
>>> 
>>> # .*, literally anything
>>> # extract first name and last name
>>> nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
>>> nameRegex.findall('First Name: Al Last Name: Sweigart')
[('Al', 'Sweigart')]
>>> 
>>> # .* is greedy search, .*? is non-greedy search
>>> serve = '<To serve humans> for dinner.>'
>>> nonGreedy = re.compile(r'<.*?>')
>>> nonGreedy.findall(serve)
['<To serve humans>']
>>> 
>>> # greedy version
>>> prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.'
>>> print(prime)
Serve the public trust.
Protect the innocent.
Upload the law.
>>> dotStar = re.compile(r'.*')
>>> dotStar.search(prime)
<_sre.SRE_Match object; span=(0, 23), match='Serve the public trust.'>
>>> # only the text before \n
>>> 
>>> # search the real whole text
>>> dotStar = re.compile(r'.*', re.DOTALL)
>>> dotStar.search(prime)
<_sre.SRE_Match object; span=(0, 61), match='Serve the public trust.\nProtect the innocent.\nU>
>>> 
>>> 
>>> # IGNORECASE, short for I
>>> vowelRegex = re.compile(r'[aeiou]')
>>> vowelRegex.findall('Al, why does your programming book talk about Robocop so much?')
['o', 'e', 'o', 'u', 'o', 'a', 'i', 'o', 'o', 'a', 'a', 'o', 'u', 'o', 'o', 'o', 'o', 'u']
>>> # only lower case
>>> 
>>> # use I
>>> vowelRegex = re.compile(r'[aeiou]',re.I)
>>> vowelRegex.findall('Al, why does your programming book talk about Robocop so much?')
['A', 'o', 'e', 'o', 'u', 'o', 'a', 'i', 'o', 'o', 'a', 'a', 'o', 'u', 'o', 'o', 'o', 'o', 'u']
>>> 
