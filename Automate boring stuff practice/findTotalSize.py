# find the total size of all files in a folders

import os

totalSize = 0

# only focuse on files
for filename in os.listdir('/Users/lichenglong/Desktop'):
    if not os.path.isfile(os.path.join('/Users/lichenglong/Desktop', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('/Users/lichenglong/Desktop', filename))

print(totalSize)
