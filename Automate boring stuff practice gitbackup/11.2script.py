>>> # read and write file
>>> helloFile = open('hello.txt')
>>> helloFile.read()
'hello fly\nhow are you ?'
>>> # treat the whole text as a string
>>> helloFile.close()
>>> 
>>> # readlines(), treat each line as a string
>>> helloFile = open('hello.txt')
>>> helloFile.readlines()
['hello fly\n', 'how are you ?']
>>> # a list of strings
>>> 
>>> # write mode
>>> helloFile = open('hello2.txt', 'w')
>>> helloFile.write('HelloJacky')
10
>>> # return how many bytes written to the file
>>> helloFile.write('HelloJacky')
10
>>> helloFile.write('HelloJacky')
10
>>> helloFile.close()
>>> # will not have \n at the end of HelloJacky
>>> 
>>> # append mode
>>> appendFile = open('hello2.txt', 'a')
>>> appendFile.write('\n\nI am the best.')
16
>>> appendFile.close()
>>> 
>>> 
>>> # store list, dictionaries in the binary file
>>> import shelve
>>> shelfFile = shelve.open('mydata')  # create some files in the directory
>>> # shelve is a like dictionary type, with keys and values
>>> shelfFile['cats'] = ['Zoe', 'Pooka', 'Simon', 'Fat-tail']
>>> shelfFile.close()
>>> 
>>> shelfFile = shelve.open('mydata')
>>> shelfFile['cats']
['Zoe', 'Pooka', 'Simon', 'Fat-tail']
>>> shelfFile.close()
>>> 
>>> shelfFile = shelve.open('mydata')
>>> shelfFile.keys()
KeysView(<shelve.DbfilenameShelf object at 0x11119f198>)
>>> list(shelfFile.keys())
['cats']
>>> list(shelfFile.values())
[['Zoe', 'Pooka', 'Simon', 'Fat-tail']]
>>> 
