>>> # copy and move
>>> import shutil
>>> # copy a file to an existed folder
>>> shutil.copy('hello.txt', 'practice move ')
'practice move /hello.txt'
>>> 
>>> # copy a file to an existed folder and rename it
>>> shutil.copy('hello.txt', 'practice move /hellojob.txt')
'practice move /hellojob.txt'
>>> 
>>> # copy a folder and rename it
>>> shutil.copytree('practice move ', 'backup')
'backup'
>>> 
>>> # move a file to a folder
>>> shutil.move('hello2.txt', 'backup')
'backup/hello2.txt'
>>> # move a file to a folder and rename it
>>> shutil.move('hello.txt', 'practice move /backup1.txt')
'practice move /backup1.txt'
>>> 
