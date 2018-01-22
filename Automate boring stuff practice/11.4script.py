>>> # delete
>>> import os
>>> # delete a single file
>>> os.unlink('trash.png')
>>> 
>>> # delete an empty directory or say folder, if not empty, warning
>>> os.rmdir('backup')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    os.rmdir('backup')
OSError: [Errno 66] Directory not empty: 'backup'
>>> 
>>> # do not send to recycling bin, permenantly delete
>>> import shutil
>>> shutil.rmtree('backup')
>>> 
>>> # do dry run before rmtree
>>> 
>>> # a safe way to delete files and folders to trashcan
>>> import send2trash
>>> send2trash.send2trash('trash1.png')
>>> 
