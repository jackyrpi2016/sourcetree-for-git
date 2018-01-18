>>> # dictionary, key: value
>>> myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
>>> # use key to get value, like look up a dictionary, search a word and find out the definition
>>> myCat['size']
'fat'
>>> # key can be numbers
>>> spam = {2: 'test', 44: 'answers'}
>>> spam
{2: 'test', 44: 'answers'}
>>> 
>>> 
>>> # list has order
>>> [1, 2, 3] == [3, 2, 1]
False
>>> # but dictionary has no order
>>> eggs = {'size': 'fat', 'color': 'gray', 'disposition': 88}
>>> ham = {'color': 'gray', 'size': 'fat', 'disposition': 88}
>>> eggs == ham
True
>>> 
>>> # in and not in, check the key
>>> 'size' in eggs
True
>>> 'xx' not in eggs
True
>>> 
>>> # dictionary is mutable, like list. hold reference
>>> 
>>> 
>>> # 3 methods for dictionary, keys(), values(), items()
>>> # want to use result as a list
>>> list(eggs.key())
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    list(eggs.key())
AttributeError: 'dict' object has no attribute 'key'
>>> list(eggs.keys())
['size', 'color', 'disposition']
>>> list(eggs.values())
['fat', 'gray', 88]
>>> list(eggs.items())
[('size', 'fat'), ('color', 'gray'), ('disposition', 88)]
>>> 
>>> # original result
>>> eggs.key()
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    eggs.key()
AttributeError: 'dict' object has no attribute 'key'
>>> eggs.keys()
dict_keys(['size', 'color', 'disposition'])
>>> eggs.values()
dict_values(['fat', 'gray', 88])
>>> eggs.items()
dict_items([('size', 'fat'), ('color', 'gray'), ('disposition', 88)])
>>> 
>>> 
>>> # good usage in for loop
>>> for k in eggs.keys():
	print(k)

	
size
color
disposition
>>> 
>>> for v in eggs.values():
	print(v)

	
fat
gray
88
>>> 
>>> for k,v in eggs.items():
	print(k, v)

	
size fat
color gray
disposition 88
>>> 
>>> # get tuples
>>> for i in eggs.items():
	print(i)

	
('size', 'fat')
('color', 'gray')
('disposition', 88)
>>> # tuples are similar to list, but they are immutable; and use () instead of []
>>> 
>>> 
>>> # 'xx' in eggs can check key; 'xx' in eggs.values() check the value
>>> eggs
{'size': 'fat', 'color': 'gray', 'disposition': 88}
>>> 'fat' in eggs.values()
True
>>> 
>>> 
>>> # to avoid checking key existence, use get()
>>> picnicItems = {'apples': 5, 'cups': 2}
>>> print('I am bringing ' + str(picnicItems('napkins', 0)) + ' to the picnic.')
>>> print('I am bringing ' + str(picnicItems('napkins', 0)) + ' to the picnic.')
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    print('I am bringing ' + str(picnicItems('napkins', 0)) + ' to the picnic.')
TypeError: 'dict' object is not callable
>>> print('I am bringing ' + str(picnicItems.get('napkins', 0)) + ' to the picnic.')
I am bringing 0 to the picnic.
>>> # if 'xx' not exist in the dictionary, return 0
>>> 
>>> 
>>> # set default value if key not exists
>>> eggs
{'size': 'fat', 'color': 'gray', 'disposition': 88}
>>> eggs.setdefault('color', 'black')
'gray'
>>> eggs
{'size': 'fat', 'color': 'gray', 'disposition': 88}
>>> eggs.setdefault('func', 'play')
'play'
>>> eggs
{'size': 'fat', 'color': 'gray', 'disposition': 88, 'func': 'play'}
>>> 
 RESTART: /Volumes/Extend/Automate boring stuff practice/dictionary_character_count.py 
{'I': 1, 't': 6, ' ': 13, 'w': 2, 'a': 4, 's': 3, 'b': 1, 'r': 5, 'i': 6, 'g': 2, 'h': 3, 'c': 3, 'o': 2, 'l': 3, 'd': 3, 'y': 1, 'n': 4, 'A': 1, 'p': 1, ',': 1, 'e': 5, 'k': 2, '.': 1}
>>> # we need transform message into uppercase, and get the right value for character
>>> 
 RESTART: /Volumes/Extend/Automate boring stuff practice/dictionary_character_count.py 
{'I': 7, 'T': 6, ' ': 13, 'W': 2, 'A': 5, 'S': 3, 'B': 1, 'R': 5, 'G': 2, 'H': 3, 'C': 3, 'O': 2, 'L': 3, 'D': 3, 'Y': 1, 'N': 4, 'P': 1, ',': 1, 'E': 5, 'K': 2, '.': 1}
>>> message
'It was a bright cold day in April, and the clocks were striking thirteen.'
>>> 
 RESTART: /Volumes/Extend/Automate boring stuff practice/dictionary_character_giant_count.py 
{' ': 241, 'R': 95, 'O': 90, 'M': 31, 'E': 152, 'A': 111, 'N': 65, 'D': 40, 'J': 3, 'U': 30, 'L': 56, 'I': 88, 'T': 108, 'S': 90, 'G': 22, 'Y': 27, 'W': 17, 'B': 22, 'H': 52, 'K': 8, 'P': 36, 'C': 39, '-': 2, 'V': 11, 'F': 29, '.': 10, "'": 3, ',': 11, 'Q': 5, '\n': 4, '1': 6, '5': 6, '6': 2, '2': 1, '7': 2, 'X': 5, '9': 3, '(': 1, ')': 1}
>>> 
>>> # want to have a nice printing result, import pprint, then use pprint.pprint()
>>> import pprint
>>> pprint.pprint(count)
{'\n': 4,
 ' ': 241,
 "'": 3,
 '(': 1,
 ')': 1,
 ',': 11,
 '-': 2,
 '.': 10,
 '1': 6,
 '2': 1,
 '5': 6,
 '6': 2,
 '7': 2,
 '9': 3,
 'A': 111,
 'B': 22,
 'C': 39,
 'D': 40,
 'E': 152,
 'F': 29,
 'G': 22,
 'H': 52,
 'I': 88,
 'J': 3,
 'K': 8,
 'L': 56,
 'M': 31,
 'N': 65,
 'O': 90,
 'P': 36,
 'Q': 5,
 'R': 95,
 'S': 90,
 'T': 108,
 'U': 30,
 'V': 11,
 'W': 17,
 'X': 5,
 'Y': 27}
>>> # want to store the above into a string instead of printing it to the screen
>>> rjtext = pprint.pformat(count)
>>> print(rjtext)
{'\n': 4,
 ' ': 241,
 "'": 3,
 '(': 1,
 ')': 1,
 ',': 11,
 '-': 2,
 '.': 10,
 '1': 6,
 '2': 1,
 '5': 6,
 '6': 2,
 '7': 2,
 '9': 3,
 'A': 111,
 'B': 22,
 'C': 39,
 'D': 40,
 'E': 152,
 'F': 29,
 'G': 22,
 'H': 52,
 'I': 88,
 'J': 3,
 'K': 8,
 'L': 56,
 'M': 31,
 'N': 65,
 'O': 90,
 'P': 36,
 'Q': 5,
 'R': 95,
 'S': 90,
 'T': 108,
 'U': 30,
 'V': 11,
 'W': 17,
 'X': 5,
 'Y': 27}
>>> 
