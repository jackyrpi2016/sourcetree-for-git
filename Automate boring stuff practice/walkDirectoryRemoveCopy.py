# walking in a directory, remove and copy files or directories

import os, shutil, re
os.chdir('/Users/lichenglong/Desktop')

for folderName, subfolders, filenames in os.walk('/Users/lichenglong/Desktop/practice move '):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))
    print()

    for subfolder in subfolders:
        # subfolder contains 'waffle'
        # do dry run in reality before removing
        # must add path !!!! os.path.join
        if 'waffle' in subfolder:
            os.rmdir(os.path.join(folderName, subfolder))
            #print(subfolder)

    for file in filenames:
        if file.endswith('.py'):
            # folderName is a filename, be sure to include path name
            # rename it, ends with .backup
            criter = re.compile(r'\w+')
            newName = criter.findall(file)
            shutil.copy(os.path.join(folderName, file), os.path.join(folderName, newName[0] + '.backup'))
