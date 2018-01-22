>>> # walking a directory tree
>>> import os
>>> for folderName, subfolders, filenames in os.walk('../Desktop/practice move '):
	print('The folder is ' + folderName)
	print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
	print('The filenames in ' + folderName + ' are: ' + str(filenames))
	print()

The folder is ../Desktop/practice move 
The subfolders in ../Desktop/practice move  are: ['delicious']
The filenames in ../Desktop/practice move  are: ['hellojob.txt', '.DS_Store', 'backup1.txt', 'hello2.txt', 'hello.txt']

The folder is ../Desktop/practice move /delicious
The subfolders in ../Desktop/practice move /delicious are: ['walnut']
The filenames in ../Desktop/practice move /delicious are: ['wrong.java', '.DS_Store']

The folder is ../Desktop/practice move /delicious/walnut
The subfolders in ../Desktop/practice move /delicious/walnut are: ['waffles']
The filenames in ../Desktop/practice move /delicious/walnut are: ['.DS_Store', 'ClearWindow.py']

The folder is ../Desktop/practice move /delicious/walnut/waffles
The subfolders in ../Desktop/practice move /delicious/walnut/waffles are: []
The filenames in ../Desktop/practice move /delicious/walnut/waffles are: []

>>> 
 RESTART: /Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py 
Traceback (most recent call last):
  File "/Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py", line 4, in <module>
    os.chcwd('/Users/lichenglong/Desktop/practice move ')
AttributeError: module 'os' has no attribute 'chcwd'
>>> 
 RESTART: /Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py 
>>> 
 RESTART: /Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py 
Traceback (most recent call last):
  File "/Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py", line 4, in <module>
    os.chdir('/Users/lichenglong/Desktop ')
FileNotFoundError: [Errno 2] No such file or directory: '/Users/lichenglong/Desktop '
>>> 
 RESTART: /Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py 
The folder is practice move 
The subfolders in practice move  are: ['delicious']
The filenames in practice move  are: ['hellojob.txt', '.DS_Store', 'backup1.txt', 'hello2.txt', 'hello.txt']

The folder is practice move /delicious
The subfolders in practice move /delicious are: ['walnut']
The filenames in practice move /delicious are: ['wrong.java', '.DS_Store']

The folder is practice move /delicious/walnut
The subfolders in practice move /delicious/walnut are: ['waffles']
The filenames in practice move /delicious/walnut are: ['.DS_Store', 'ClearWindow.py']

Traceback (most recent call last):
  File "/Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py", line 16, in <module>
    os.rmdir(subfolder)
FileNotFoundError: [Errno 2] No such file or directory: 'waffles'
>>> os.getcwd
<built-in function getcwd>
>>> os.getcwd()
'/Users/lichenglong/Desktop'
>>> 
 RESTART: /Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py 
The folder is /Users/lichenglong/Desktop/practice move 
The subfolders in /Users/lichenglong/Desktop/practice move  are: ['delicious']
The filenames in /Users/lichenglong/Desktop/practice move  are: ['hellojob.txt', '.DS_Store', 'backup1.txt', 'hello2.txt', 'hello.txt']

The folder is /Users/lichenglong/Desktop/practice move /delicious
The subfolders in /Users/lichenglong/Desktop/practice move /delicious are: ['walnut']
The filenames in /Users/lichenglong/Desktop/practice move /delicious are: ['wrong.java', '.DS_Store']

The folder is /Users/lichenglong/Desktop/practice move /delicious/walnut
The subfolders in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['waffles']
The filenames in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['.DS_Store', 'ClearWindow.py']

Traceback (most recent call last):
  File "/Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py", line 16, in <module>
    os.rmdir(subfolder)
FileNotFoundError: [Errno 2] No such file or directory: 'waffles'
>>> 
 RESTART: /Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py 
The folder is /Users/lichenglong/Desktop/practice move 
The subfolders in /Users/lichenglong/Desktop/practice move  are: ['delicious']
The filenames in /Users/lichenglong/Desktop/practice move  are: ['hellojob.txt', '.DS_Store', 'backup1.txt', 'hello2.txt', 'hello.txt']

The folder is /Users/lichenglong/Desktop/practice move /delicious
The subfolders in /Users/lichenglong/Desktop/practice move /delicious are: ['walnut']
The filenames in /Users/lichenglong/Desktop/practice move /delicious are: ['wrong.java', '.DS_Store']

The folder is /Users/lichenglong/Desktop/practice move /delicious/walnut
The subfolders in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['waffles']
The filenames in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['.DS_Store', 'ClearWindow.py']

Traceback (most recent call last):
  File "/Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py", line 16, in <module>
    os.rmdir(subfolder)
FileNotFoundError: [Errno 2] No such file or directory: 'waffles'
>>> 
 RESTART: /Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py 
The folder is /Users/lichenglong/Desktop/practice move 
The subfolders in /Users/lichenglong/Desktop/practice move  are: ['delicious']
The filenames in /Users/lichenglong/Desktop/practice move  are: ['hellojob.txt', '.DS_Store', 'backup1.txt', 'hello2.txt', 'hello.txt']

The folder is /Users/lichenglong/Desktop/practice move /delicious
The subfolders in /Users/lichenglong/Desktop/practice move /delicious are: ['walnut']
The filenames in /Users/lichenglong/Desktop/practice move /delicious are: ['wrong.java', '.DS_Store']

The folder is /Users/lichenglong/Desktop/practice move /delicious/walnut
The subfolders in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['waffles']
The filenames in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['.DS_Store', 'ClearWindow.py']

Traceback (most recent call last):
  File "/Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py", line 15, in <module>
    os.rmdir(subfolder)
FileNotFoundError: [Errno 2] No such file or directory: 'waffles'
>>> 
 RESTART: /Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py 
The folder is /Users/lichenglong/Desktop/practice move 
The subfolders in /Users/lichenglong/Desktop/practice move  are: ['delicious']
The filenames in /Users/lichenglong/Desktop/practice move  are: ['hellojob.txt', '.DS_Store', 'backup1.txt', 'hello2.txt', 'hello.txt']

The folder is /Users/lichenglong/Desktop/practice move /delicious
The subfolders in /Users/lichenglong/Desktop/practice move /delicious are: ['walnut']
The filenames in /Users/lichenglong/Desktop/practice move /delicious are: ['wrong.java', '.DS_Store']

The folder is /Users/lichenglong/Desktop/practice move /delicious/walnut
The subfolders in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['waffles']
The filenames in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['.DS_Store', 'ClearWindow.py']

Traceback (most recent call last):
  File "/Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py", line 16, in <module>
    os.rmdir(subfolder)
FileNotFoundError: [Errno 2] No such file or directory: 'waffles'
>>> 
 RESTART: /Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py 
The folder is /Users/lichenglong/Desktop/practice move 
The subfolders in /Users/lichenglong/Desktop/practice move  are: ['delicious']
The filenames in /Users/lichenglong/Desktop/practice move  are: ['hellojob.txt', '.DS_Store', 'backup1.txt', 'hello2.txt', 'hello.txt']

The folder is /Users/lichenglong/Desktop/practice move /delicious
The subfolders in /Users/lichenglong/Desktop/practice move /delicious are: ['walnut']
The filenames in /Users/lichenglong/Desktop/practice move /delicious are: ['wrong.java', '.DS_Store']

The folder is /Users/lichenglong/Desktop/practice move /delicious/walnut
The subfolders in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['waffles']
The filenames in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['.DS_Store', 'ClearWindow.py']

waffles
Traceback (most recent call last):
  File "/Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py", line 23, in <module>
    shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup'))
NameError: name 'shutil' is not defined
>>> 
 RESTART: /Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py 
The folder is /Users/lichenglong/Desktop/practice move 
The subfolders in /Users/lichenglong/Desktop/practice move  are: ['delicious']
The filenames in /Users/lichenglong/Desktop/practice move  are: ['hellojob.txt', '.DS_Store', 'backup1.txt', 'hello2.txt', 'hello.txt']

The folder is /Users/lichenglong/Desktop/practice move /delicious
The subfolders in /Users/lichenglong/Desktop/practice move /delicious are: ['walnut']
The filenames in /Users/lichenglong/Desktop/practice move /delicious are: ['wrong.java', '.DS_Store']

The folder is /Users/lichenglong/Desktop/practice move /delicious/walnut
The subfolders in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['waffles']
The filenames in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['.DS_Store', 'ClearWindow.py']

waffles
Traceback (most recent call last):
  File "/Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py", line 23, in <module>
    shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup'))
AttributeError: module 'os' has no attribute 'join'
>>> import shutil
>>> 
 RESTART: /Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py 
The folder is /Users/lichenglong/Desktop/practice move 
The subfolders in /Users/lichenglong/Desktop/practice move  are: ['delicious']
The filenames in /Users/lichenglong/Desktop/practice move  are: ['hellojob.txt', '.DS_Store', 'backup1.txt', 'hello2.txt', 'hello.txt']

The folder is /Users/lichenglong/Desktop/practice move /delicious
The subfolders in /Users/lichenglong/Desktop/practice move /delicious are: ['walnut']
The filenames in /Users/lichenglong/Desktop/practice move /delicious are: ['wrong.java', '.DS_Store']

The folder is /Users/lichenglong/Desktop/practice move /delicious/walnut
The subfolders in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['waffles']
The filenames in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['.DS_Store', 'ClearWindow.py']

waffles
The folder is /Users/lichenglong/Desktop/practice move /delicious/walnut/waffles
The subfolders in /Users/lichenglong/Desktop/practice move /delicious/walnut/waffles are: []
The filenames in /Users/lichenglong/Desktop/practice move /delicious/walnut/waffles are: []

>>> 
 RESTART: /Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py 
The folder is /Users/lichenglong/Desktop/practice move 
The subfolders in /Users/lichenglong/Desktop/practice move  are: ['delicious']
The filenames in /Users/lichenglong/Desktop/practice move  are: ['hellojob.txt', '.DS_Store', 'backup1.txt', 'hello2.txt', 'hello.txt']

The folder is /Users/lichenglong/Desktop/practice move /delicious
The subfolders in /Users/lichenglong/Desktop/practice move /delicious are: ['walnut']
The filenames in /Users/lichenglong/Desktop/practice move /delicious are: ['wrong.java', '.DS_Store']

The folder is /Users/lichenglong/Desktop/practice move /delicious/walnut
The subfolders in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['waffles']
The filenames in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['.DS_Store', 'ClearWindow.py', 'ClearWindow.py.backup']

waffles
The folder is /Users/lichenglong/Desktop/practice move /delicious/walnut/waffles
The subfolders in /Users/lichenglong/Desktop/practice move /delicious/walnut/waffles are: []
The filenames in /Users/lichenglong/Desktop/practice move /delicious/walnut/waffles are: []

>>> 
 RESTART: /Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py 
The folder is /Users/lichenglong/Desktop/practice move 
The subfolders in /Users/lichenglong/Desktop/practice move  are: ['delicious']
The filenames in /Users/lichenglong/Desktop/practice move  are: ['hellojob.txt', '.DS_Store', 'backup1.txt', 'hello2.txt', 'hello.txt']

The folder is /Users/lichenglong/Desktop/practice move /delicious
The subfolders in /Users/lichenglong/Desktop/practice move /delicious are: ['walnut']
The filenames in /Users/lichenglong/Desktop/practice move /delicious are: ['wrong.java', '.DS_Store']

The folder is /Users/lichenglong/Desktop/practice move /delicious/walnut
The subfolders in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['waffles']
The filenames in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['.DS_Store', 'ClearWindow.py', 'ClearWindow.py.backup']

waffles
Traceback (most recent call last):
  File "/Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py", line 25, in <module>
    shutil.copy(os.path.join(folderName, file), os.path.join(folderName, newName + '.backup'))
TypeError: can only concatenate list (not "str") to list
>>> print(newName)
['ClearWindow', 'py']
>>> 
 RESTART: /Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py 
The folder is /Users/lichenglong/Desktop/practice move 
The subfolders in /Users/lichenglong/Desktop/practice move  are: ['delicious']
The filenames in /Users/lichenglong/Desktop/practice move  are: ['hellojob.txt', '.DS_Store', 'backup1.txt', 'hello2.txt', 'hello.txt']

The folder is /Users/lichenglong/Desktop/practice move /delicious
The subfolders in /Users/lichenglong/Desktop/practice move /delicious are: ['walnut']
The filenames in /Users/lichenglong/Desktop/practice move /delicious are: ['wrong.java', '.DS_Store']

The folder is /Users/lichenglong/Desktop/practice move /delicious/walnut
The subfolders in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['waffles']
The filenames in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['.DS_Store', 'ClearWindow.py', 'ClearWindow.py.backup']

waffles
Traceback (most recent call last):
  File "/Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py", line 25, in <module>
    shutil.copy(os.path.join(folderName, file), os.path.join(folderName, newName + '.backup'))
TypeError: can only concatenate list (not "str") to list
>>> print(newName)
['ClearWindow', 'py']
>>> 
 RESTART: /Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py 
The folder is /Users/lichenglong/Desktop/practice move 
The subfolders in /Users/lichenglong/Desktop/practice move  are: ['delicious']
The filenames in /Users/lichenglong/Desktop/practice move  are: ['hellojob.txt', '.DS_Store', 'backup1.txt', 'hello2.txt', 'hello.txt']

The folder is /Users/lichenglong/Desktop/practice move /delicious
The subfolders in /Users/lichenglong/Desktop/practice move /delicious are: ['walnut']
The filenames in /Users/lichenglong/Desktop/practice move /delicious are: ['wrong.java', '.DS_Store']

The folder is /Users/lichenglong/Desktop/practice move /delicious/walnut
The subfolders in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['waffles']
The filenames in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['.DS_Store', 'ClearWindow.py', 'ClearWindow.py.backup']

waffles
Traceback (most recent call last):
  File "/Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py", line 25, in <module>
    shutil.copy(os.path.join(folderName, file), os.path.join(folderName, newName(1) + '.backup'))
TypeError: 'list' object is not callable
>>> print(newName)
['ClearWindow', 'py']
>>> newName(1)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    newName(1)
TypeError: 'list' object is not callable
>>> newName[1]
'py'
>>> newName[10
	]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    newName[10
IndexError: list index out of range
>>> newName[0]
'ClearWindow'
>>> 
 RESTART: /Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py 
The folder is /Users/lichenglong/Desktop/practice move 
The subfolders in /Users/lichenglong/Desktop/practice move  are: ['delicious']
The filenames in /Users/lichenglong/Desktop/practice move  are: ['hellojob.txt', '.DS_Store', 'backup1.txt', 'hello2.txt', 'hello.txt']

The folder is /Users/lichenglong/Desktop/practice move /delicious
The subfolders in /Users/lichenglong/Desktop/practice move /delicious are: ['walnut']
The filenames in /Users/lichenglong/Desktop/practice move /delicious are: ['wrong.java', '.DS_Store']

The folder is /Users/lichenglong/Desktop/practice move /delicious/walnut
The subfolders in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['waffles']
The filenames in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['.DS_Store', 'ClearWindow.py', 'ClearWindow.py.backup']

waffles
The folder is /Users/lichenglong/Desktop/practice move /delicious/walnut/waffles
The subfolders in /Users/lichenglong/Desktop/practice move /delicious/walnut/waffles are: []
The filenames in /Users/lichenglong/Desktop/practice move /delicious/walnut/waffles are: []

>>> 
 RESTART: /Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py 
The folder is /Users/lichenglong/Desktop/practice move 
The subfolders in /Users/lichenglong/Desktop/practice move  are: ['delicious']
The filenames in /Users/lichenglong/Desktop/practice move  are: ['hellojob.txt', '.DS_Store', 'backup1.txt', 'hello2.txt', 'hello.txt']

The folder is /Users/lichenglong/Desktop/practice move /delicious
The subfolders in /Users/lichenglong/Desktop/practice move /delicious are: ['walnut']
The filenames in /Users/lichenglong/Desktop/practice move /delicious are: ['wrong.java', '.DS_Store']

The folder is /Users/lichenglong/Desktop/practice move /delicious/walnut
The subfolders in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['waffles']
The filenames in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['.DS_Store', 'ClearWindow.py', 'ClearWindow.py.backup']

Traceback (most recent call last):
  File "/Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py", line 16, in <module>
    os.rmdir(subfolder)
FileNotFoundError: [Errno 2] No such file or directory: 'waffles'
>>> 
 RESTART: /Volumes/Extend/Automate boring stuff practice/walkDirectoryRemoveCopy.py 
The folder is /Users/lichenglong/Desktop/practice move 
The subfolders in /Users/lichenglong/Desktop/practice move  are: ['delicious']
The filenames in /Users/lichenglong/Desktop/practice move  are: ['hellojob.txt', '.DS_Store', 'backup1.txt', 'hello2.txt', 'hello.txt']

The folder is /Users/lichenglong/Desktop/practice move /delicious
The subfolders in /Users/lichenglong/Desktop/practice move /delicious are: ['walnut']
The filenames in /Users/lichenglong/Desktop/practice move /delicious are: ['wrong.java', '.DS_Store']

The folder is /Users/lichenglong/Desktop/practice move /delicious/walnut
The subfolders in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['waffles']
The filenames in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['.DS_Store', 'ClearWindow.py', 'ClearWindow.py.backup']

>>> 
