
>>> # string is immutable, so itself cannot be changed or modified
>>> # upper()   lower()
>>> spam = 'Hello world!'
>>> 
>>> # spam will not be changed, unless
>>> spam.upper()
'HELLO WORLD!'
>>> spam
'Hello world!'
>>> spam = spam.upper()
>>> spam
'HELLO WORLD!'
>>> 
>>> # lower()
>>> spam.lower()
'hello world!'
>>> 
>>> 
>>> # extremely helpful when we need to compare input and stored string
>>> answer = input()
YES
>>> answer
'YES'
>>> if answer.lower() == 'yes':
	print('Playing again')

	
Playing again
>>> 
>>> 
>>> # check methods, isupper()   islower()
>>> # islower, if one character is uppere, returns false
>>> spam = 'Hello'
>>> spam.islower()
False
>>> # same with isupper()
>>> 
>>> # '', '12345' returns false, because no character is found
>>> spam = ''
>>> spam.islower()
False
>>> spam.isupper()
False
>>> 
>>> 
>>> # isalpha(), only letters
>>> 'hello'.isalpha()
True
>>> 'hello123'.isalpha()
False
>>> # isalnum(), num or letter are ok
>>> 
>>> '123'.isalnum()
True
>>> 'hello123'.isalnum()
True
>>> # isdecimal(), num only
>>> '123'.isdecimal()
True
>>> # isspace(), whitespace only
>>> '   '.isspace()
True
>>> 'hello world'.isspace()
False
>>> # istitle(), first letter is uppercase for each word in the sentence
>>> 'That Is Cat'.istitle()
True
>>> # title(), change sentence into title format
>>> 'hello world!'.title()
'Hello World!'
>>> 
>>> 
>>> # startswith() and endswith()
>>> # startswith()
>>> 'Hello world!'.startswith('H')
True
>>> 'Hello world!'.startswith('Hello')
True
>>> 'Hello world!'.startswith('Hello ')
True
>>> # endswith()
>>> 'Hello world!'.endswith('world!')
True
>>> 'Hello world!'.endswith('world')
False
>>> 
>>> 
>>> 
>>> 
>>> # join(), use 'x' to interpolate and join other strings
>>> ','.join(['cats', 'rats', 'bats'])
'cats,rats,bats'
>>> ''.join(['cats', 'rats', 'bats'])
'catsratsbats'
>>> ' '.join(['cats', 'rats', 'bats'])
'cats rats bats'
>>> '\n\n'.join(['cats', 'rats', 'bats'])
'cats\n\nrats\n\nbats'
>>> # we must use print to see \n effect
>>> print('\n\n'.join(['cats', 'rats', 'bats']))
cats

rats

bats
>>> 
>>> 
>>> # split(), default whitespace
>>> 'My name is Simon'.split()
['My', 'name', 'is', 'Simon']
>>> # split on 'm', !!! lower 'm' not include upper 'M', it will not show '
>>> # split on 'm', !!! lower 'm' not include upper 'M', it will not show 'm' in the slices
>>> 'My name is Simon'.split('m')
['My na', 'e is Si', 'on']
>>> 
>>> 
>>> # rjust(), ljust(); satisfy the length, also put string in the right or in the left
>>> 'Hello'.rjust(10)
'     Hello'
>>> 'Hello'.ljust(10)
'Hello     '
>>> # change character, second parameter
>>> 'Hello'.rjust(10, '=')
'=====Hello'
>>> 'Hello'.ljust(10, '*')
'Hello*****'
>>> # center()
>>> 'Hello'.center(10, '=')
'==Hello==='
>>> name = 'jacky'
>>> name.center(20, '-')
'-------jacky--------'
>>> 
>>> 
>>> # strip(), lstrip(), rstrip()
>>> spam.rjust(10)
'          '
>>> spam = 'Hello'
>>> spam.rjust(10)
'     Hello'
>>> spam = spam.rjust(10)
>>> spam
'     Hello'
>>> spam.strip()
'Hello'
>>> 
>>> '      x      '.strip()
'x'
>>> '      x      '.lstrip()
'x      '
>>> '      x      '.rstrip()
'      x'
>>> 
>>> # strip specified letters, order is not important
>>> 'SpamSpamBaconSapmEggsSpamSpam'.strip('ampS')
'BaconSapmEggs'
>>> # it removes a, m, p and S, it operates on both sides, stops when encountering not specified letters
>>> spam = 'Hello world!'
>>> # replace()
>>> spam.replace('e', 'XYZ')
'HXYZllo world!'
>>> 
>>> 
>>> 
>>> 
>>> # pyperclip module
>>> # can copy and paste to or from clipboard
>>> # it is not included in the python, --> pip install pyperclip
>>> # check by import pyperclip
>>> import pyperclip
>>> # send text to clipboard
>>> pyperclip.copy('hello')
>>> pyperclip.paste()
'hello'
>>> 
