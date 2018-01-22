>>> # tricks with text
>>> 'That is jacky's cat'
SyntaxError: invalid syntax
>>> 
>>> # we can use " if we want to include '
>>> "That is jacky's cat"
"That is jacky's cat"
>>> # but if we want to include " and ', use escape character \
>>> 'Say hi to Bob\'s sister.'
"Say hi to Bob's sister."
>>> 
>>> # example of those \', \", \t #tab, \n #new line, \\ # just the backslash
>>> print('Hello there!\nHow are you?\nI\'m fine.')
Hello there!
How are you?
I'm fine.
>>> 
>>> 
>>> # raw string, preview of regular expression
>>> r'Hello'
'Hello'
>>> r'That is Carol\'s cat'
"That is Carol\\'s cat"
>>> # the above is a regular, non-raw string value
>>> 
>>> print(r'That is Carol\'s cat')
That is Carol\'s cat
>>> 
>>> 
>>> # multiline strings with triple quotes, like ''' or """
>>> """Dear jacky,
I am you from the future. Today is 11/03 2017, you will be successful in the future as a programmer.
Yours
chenglong li"""
'Dear jacky,\nI am you from the future. Today is 11/03 2017, you will be successful in the future as a programmer.\nYours\nchenglong li'
>>> # python automatically insert \n and other \ into the string
>>> 
>>> 
>>> # recap the similarities between list and string
>>> 'Hello world!'
'Hello world!'
>>> spam = 'Hello world!'
>>> # index
>>> spam[0]
'H'
>>> # slice
>>> spam[1:5]
'ello'
>>> # negative index
>>> spam[-1]
'!'
>>> # in and not in
>>> 'Hello' in spam
True
>>> 'x' not in spam
True
>>> # it is Case sensative
>>> 'HELLO' in spam
False
>>> 
