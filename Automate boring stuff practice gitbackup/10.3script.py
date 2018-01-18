>>> # continue on searching in the text
>>> import re
>>> batRegex = re.compile(r'Bat(wo)?man')
>>> # (...)? means, it can be Batwoman or Batman. But can only appear once or not
>>> mo = batRegex.search('The adventure of Batman')
>>> mo.group()
'Batman'
>>> 
>>> mo = batRegex.search('The adventure of Batwoman')
>>> mo.group()
'Batwoman'
>>> 
>>> # can not search for 'wo' more than one time
>>> mo = batRegex.search('The adventure of Batwowowoman')
>>> mo.group()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    mo.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> mo == None
True
>>> 
>>> 
>>> # match phone number with area code or not
>>> phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
>>> mo.group()
'415-555-1234'
>>> 
>>> phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
>>> mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
>>> mo.group()
'555-1234'
>>> 
>>> 
>>> # if want to use '?', \?
>>> 
>>> 
>>> # *, 0 or more times
>>> batRegex = re.compile(r'Bat(wo)*man')
>>> mo = batRegex.search('The adventure of Batwowowoman')
>>> mo.group()
'Batwowowoman'
>>> 
>>> 
>>> # if want to use '*', \*
>>> 
>>> 
>>> # +, at least 1 or more times
>>> batRegex = re.compile(r'Bat(wo)+man')
>>> mo = batRegex.search('The adventure of Batman')
>>> mo == None
True
>>> 
>>> # at least one time
>>> mo = batRegex.search('The adventure of Batwowowoman')
>>> mo.group()
'Batwowowoman'
>>> 
>>> 
>>> # '+', \+
>>> 
>>> 
>>> regex = re.compile(r'\+\*\?')
>>> mo = regex.search('I learned about +*? regex syntax')
>>> mo.group()
'+*?'
>>> 
>>> regex = re.compile(r'(\+\*\?)+')
>>> # \+\*\? at least one time
>>> mo = regex.search('I learned about +*?+*?+*?+*? regex syntax')
>>> mo.group()
'+*?+*?+*?+*?'
>>> 
>>> 
>>> # {x}, specific time
>>> haRegex = re.compile(r'(Ha){3}')  # 3 times
>>> mo = haRegex.search('He said "HaHaHa"')
>>> mo.group()
'HaHaHa'
>>> 
>>> # match 3 phone number with or without area code,
>>> phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
>>> mo = phoneRegex.search('My phone number is 415-555-1234,555-4242,212-555-0000')
>>> mo.group()
'415-555-1234,555-4242,212-555-0000'
>>> 
>>> 
>>> # {x,y} at least x, at most y
>>> haRegex = re.compile(r'(Ha){3,5}')
>>> mo = haRegex.search('He said "HaHaHa"')
>>> mo.group()
'HaHaHa'
>>> mo = haRegex.search('He said "HaHaHaHaHa"')
>>> mo.group()
'HaHaHaHaHa'
>>> mo = haRegex.search('He said "HaHaHaHaHaHa"')
>>> mo.group()
'HaHaHaHaHa'
>>> # even 6 Ha, it can still take out 5, the max of 3 to 5
>>> # haRegex = re.compile(r'(Ha){3,}') means equal or more than 3
>>> 
>>> 
>>> # default for search is greedy match, use ? to turn into non-greedy
>>> digitRegex = re.compile(r'(\d){3,5}')
>>> digitRegex.search('1234567890')
<_sre.SRE_Match object; span=(0, 5), match='12345'>
>>> mo = digitRegex.search('1234567890')
>>> mo.group()
'12345'
>>> 
>>> # non greedy
>>> digitRegex = re.compile(r'(\d){3,5}?')
>>> mo = digitRegex.search('1234567890')
>>> mo.group()
'123'
>>> 
