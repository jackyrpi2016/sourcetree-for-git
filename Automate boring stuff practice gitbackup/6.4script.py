
>>> list('Hello')
['H', 'e', 'l', 'l', 'o']
>>> 
>>> # list and string are similar
>>> name = 'Zophie'
>>> # index
>>> name[0]
'Z'
>>> # slices
>>> name[1:3]
'op'
>>> # negative index
>>> name[-1]
'e'
>>> # in
>>> 'Zo' in name
True
>>> for letter in name:
	print(letter)

	
Z
o
p
h
i
e
>>> 
>>> 
>>> 
>>> # difference, list is mutable datatype which means it can be added, removed or changed
>>> # string is immutable datatype which means it can not be changed
>>> name
'Zophie'
>>> name[1] = 'x'
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    name[1] = 'x'
TypeError: 'str' object does not support item assignment
>>> 
>>> 
>>> 
>>> 
>>> # we can create new string from old string using slices
>>> name = 'Zophie a cat'
>>> newName = name[0:7] + 'the' + [8:12]
SyntaxError: invalid syntax
>>> newName = name[0:7] + 'the' + [8:12]
SyntaxError: invalid syntax
>>> newName = name[0:7] + 'the' + name[8:12]
>>> newName
'Zophie the cat'
>>> 
>>> 
>>> # the difference between mutable and immutable,     'reference'
>>> # list gives reference to others, when assigning variable
>>> spam = [0, 1, 2, 3, 4, 5]
>>> cheese = spam
>>> cheese[1] = 'Hello'
>>> cheese
[0, 'Hello', 2, 3, 4, 5]
>>> spam
[0, 'Hello', 2, 3, 4, 5]
>>> 
 RESTART: /Volumes/Extend/Automate boring stuff practice/immutable_attention.py 
[1, 2, 3, 'hello']
>>> # just giving reference saves a lot of storage
>>> 
>>> # what if we want a new copy of the original
>>> import copy
>>> spam = [0, 1, 2, 3, 4, 5]
>>> cheese = copy.deepcopy(spam)
>>> cheese[1] = 42
>>> cheese
[0, 42, 2, 3, 4, 5]
>>> spam
[0, 1, 2, 3, 4, 5]
>>> 
>>> 
>>> 
>>> 
>>> # line continuation
>>> # python recognizes a line continues
>>> spam = ['a'
	    'b'
	    'c']
>>> # \ is the line continuation symbol
>>> print('Four score and seven ' + \
      'years ago')
Four score and seven years ago
>>> 
