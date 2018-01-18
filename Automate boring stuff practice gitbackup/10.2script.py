>>> # continue on phone number
>>> import re
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> mo = phoneNumRegex.search('My number is 415-555-4242')
>>> mo.group()
'415-555-4242'
>>> 
>>> # use() to separate group elements
>>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
>>> mo = phoneNumRegex.search('My number is 415-555-4242')
>>> mo.group()
'415-555-4242'
>>> mo.group(1)
'415'
>>> mo.group(2)
'555-4242'
>>> 
>>> # find (415) 555-4242
>>> # use \(...\)
>>> phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
>>> mo = phoneNumRegex.search('My number is (415) 555-4242')
>>> mo.group()
'(415) 555-4242'
>>> 
>>> 
>>> # pipe character
>>> batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
>>> mo = batRegex.search('Batmobile lost a wheel')
>>> mo.group()
'Batmobile'
>>> 
>>> # find something not in the format, return None
>>> mo = batRegex.search('Batmotocycle lost a wheel')
>>> mo == None
True
>>> mo.group()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    mo.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> 
>>> # make sure what group has been found
>>> mo = batRegex.search('Batmobile lost a wheel')
>>> mo.group(1)
'mobile'
>>> 
