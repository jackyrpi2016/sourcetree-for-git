>>> # directory, absolute and relative path
>>> import os
>>> os.path.join('folder1', 'folder2', 'file.png')
'folder1/folder2/file.png'
>>> 
>>> # os.sep: determine the separator
>>> os.sep
'/'
>>> 
>>> # get current directory
>>> os.getcwd()
'/Users/lichenglong/Documents'
>>> 
>>> # change current directory
>>> os.chdir('/Users/lichenglong/Desktop')
>>> os.getcwd()
'/Users/lichenglong/Desktop'
>>> 
>>> # absolute path and relative path
>>> os.path.abspath('wrong.java')
'/Users/lichenglong/Desktop/wrong.java'
>>> 
>>> # conceal some info, use ../../ and so on
>>> os.path.abspath('../../wrong.java')
'/Users/wrong.java'
>>> os.path.isabs('../../wrong.java')
False
>>> os.path.isabs('./Users/lichenglong/Desktop/wrong.java')
False
>>> os.path.isabs('/Users/lichenglong/Desktop/wrong.java')
True
>>> 
>>> # relative path
>>> os.path.relpath('/Users/lichenglong/Desktop/wrong.java', '/Users')
'lichenglong/Desktop/wrong.java'
>>> # the relative path with the starting point
>>> 
>>> # dirname, directory path; basename, file name
>>> os.path.dirname('/Users/lichenglong/Desktop/wrong.java')
'/Users/lichenglong/Desktop'
>>> os.path.basename('/Users/lichenglong/Desktop/wrong.java')
'wrong.java'
>>> 
>>> # path.exists; path.isfile; path.isdir
>>> os.path.exists('/Users/lichenglong/Desktop/wrong.java')
True
>>> os.path.isfile('/Users/lichenglong/Desktop/wrong.java')
True
>>> os.path.isdir('/Users/lichenglong/Desktop/wrong.java')
False
>>> os.path.isdir('/Users/lichenglong/Desktop')
True
>>> 
>>> # get size of the file
>>> os.path.getsize('/Users/lichenglong/Desktop/wrong.java')
2638
>>> # in bytes
>>> 
>>> os.listdir('/Users/lichenglong/Desktop)
	   
== RESTART: /Volumes/Extend/Automate boring stuff practice/findTotalSize.py ==
5009948
>>> 
>>> # create new folders
>>> os.makedirs('/Users/lichenglong/Desktop/delicious/walnut/waffles')
>>> 
