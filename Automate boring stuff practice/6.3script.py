>>> # method is different from function, method is attached to a certain value. the example, we must use spam.index(), not index() !!
>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> spam.index('hi')
1
>>> 
>>> 
>>> 
>>> 
>>> # append and insert to add values
>>> # append add at the end of list
>>> spam = ['cat', 'dog', 'bat']
>>> spam.append('moose')
>>> spam
['cat', 'dog', 'bat', 'moose']
>>> 
>>> # insert can be anywhere, the items after this index will move backwards
>>> spam.insert(2, 'girl')
>>> spam
['cat', 'dog', 'girl', 'bat', 'moose']
>>> 
>>> 
>>> # string datatype, no append
>>> eggs = 'hello'
>>> eggs.append('world')
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    eggs.append('world')
AttributeError: 'str' object has no attribute 'append'
>>> 
>>> 
>>> 
>>> 
>>> # remove, indicate the value; del, speicfy index
>>> spam = ['cat', 'dog', 'bat', 'rat']
>>> spam.remove('bat')
>>> spam
['cat', 'dog', 'rat']
>>> 
>>> del spam[1]
>>> spam
['cat', 'rat']
>>> 
>>> # remove can only remove the first item
>>> spam = ['cat', 'dog', 'bat', 'rat', 'dog']
>>> spam.remove('dog')
>>> spam
['cat', 'bat', 'rat', 'dog']
>>> 
>>> 
>>> 
>>> 
>>> # sort, apply to integer and string. sort on ASCII-betical order, pretty much same as alphabetical order
>>> spam = [2, -1, 124, 7, 0]
>>> spam.sort()
>>> spam
[-1, 0, 2, 7, 124]
>>> 
>>> spam = ['cat', 'bat', 'dog', 'rat', 'elephant']
>>> spam.sort(reverse=True)
>>> spam
['rat', 'elephant', 'dog', 'cat', 'bat']
>>> 
>>> 
>>> # not suitable when list has different datatypes
>>> spam = [1, 2, 3, 'Alice', 'Bob']
>>> spam.sort()
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    spam.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> 
>>> 
>>> # ASCII-betical order, uppercase come before lowercase
>>> spam = ['a', 'z', 'A', 'Z']
>>> spam.sort()
>>> spam
['A', 'Z', 'a', 'z']
>>> # solution to sort string with upper and lower case
>>> spam.sort(key = str.lower)
>>> spam
['A', 'a', 'Z', 'z']
>>> # transform uppercase to lowercase when sorting
