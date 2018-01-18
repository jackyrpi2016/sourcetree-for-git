>>> # walking in a directory
>>> import os
>>> for folderName, subfolders, filenames in os.walk('/Users/lichenglong/Desktop/practice move '):
	print('The folder is ' + folderName)
	print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
	print('The filenames in ' + folderName + ' are: ' + str(filenames))
	print()

The folder is /Users/lichenglong/Desktop/practice move 
The subfolders in /Users/lichenglong/Desktop/practice move  are: ['delicious']
The filenames in /Users/lichenglong/Desktop/practice move  are: ['hellojob.txt', '.DS_Store', 'backup1.txt', 'hello2.txt', 'hello.txt']

The folder is /Users/lichenglong/Desktop/practice move /delicious
The subfolders in /Users/lichenglong/Desktop/practice move /delicious are: ['walnut']
The filenames in /Users/lichenglong/Desktop/practice move /delicious are: ['wrong.java', '.DS_Store']

The folder is /Users/lichenglong/Desktop/practice move /delicious/walnut
The subfolders in /Users/lichenglong/Desktop/practice move /delicious/walnut are: []
The filenames in /Users/lichenglong/Desktop/practice move /delicious/walnut are: ['.DS_Store', 'ClearWindow.py', 'ClearWindow.py.backup', 'ClearWindow.backup']

>>> 
