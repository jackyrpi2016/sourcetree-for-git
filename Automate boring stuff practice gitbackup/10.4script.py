>>> # findall
>>> import re
>>> phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> phoneRegex
re.compile('\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d')
>>> 
>>> # store large text in the variable with '''  '''
>>> resume = ''' Jacky
cell: 508-555-5555,  Home: 508-555-1234

sdfjsad;gvnkdsagjadsajgla;sdklnfsdakl
jldsfkjdsf

jdsklfjlsjfsdjskl

'''
>>> phoneRegex.search(resume)
<_sre.SRE_Match object; span=(13, 25), match='508-555-5555'>
>>> # search(), return a match object
>>> 
>>> phoneRegex.findall(resume)
['508-555-5555', '508-555-1234']
>>> # findall(), return a list of strings
>>> 
>>> # compile has more than 1 group, return tuple of strings
>>> phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
>>> phoneRegex.findall(resume)
[('508', '555-5555'), ('508', '555-1234')]
>>> 
>>> # 3 groups, and group contains group
>>> phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
>>> phoneRegex.findall(resume)
[('508-555-5555', '508', '555-5555'), ('508-555-1234', '508', '555-1234')]
>>> 
>>> 
>>> 
>>> 
>>> # character class, \d is numeric digit from 0 - 9
>>> lyrics = '12 Drummers Drumming, 11 Pipers Piping, 10 Lords a Leaping, 9 Ladies Dancing, 8 Maids a Milking, 7 Swans a Swimming, 6 Geese a Laying, 5 Golden Rings, 4 Calling Birds, 3 French Hens, 2 Turtle Doves and 1 Partridge in a Pear Tree'
>>> xmasRegex = re.compile(r'\d+\s\w+')  # \d+: 1 or more, \s: whitespac, \w+: 1 or more words
>>> xmasRegex.findall(lyrics)
['12 Drummers', '11 Pipers', '10 Lords', '9 Ladies', '8 Maids', '7 Swans', '6 Geese', '5 Golden', '4 Calling', '3 French', '2 Turtle', '1 Partridge']
>>> 
>>> 
>>> # make your own character class
>>> vowelRegex = re.compile(r'[aeiou]')
>>> alphaRegex = re.compile('[a-z]')  # a to z
>>> alphaRegex = re.compile('[a-zA-F]')  # a to z and A to F
>>> # must include capital words
>>> vowelRegex = re.compile(r'[aeiouAEIOU]')
>>> vowelRegex.findall('Robocop eats baby food.')
['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o']
>>> 
>>> # find two vowels in a row, double vowel
>>> doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
>>> doubleVowelRegex.findall('Robocop eats baby food.')
['ea', 'oo']
>>> 
>>> 
>>> # negative character class
>>> consonantsRegex = re.compile(r'[^aeiouAEIOU]')  # anything that is not in there, including punctuations
>>> consonantsRegex.findall('Robocop eats baby food.')
['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.']
>>> 
