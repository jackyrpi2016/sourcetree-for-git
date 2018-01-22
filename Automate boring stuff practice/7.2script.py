>>> # create a dictionary element
>>> cat = {'name': 'jacky', 'age': 7, 'color': 'gray'}
>>> allCats = []
>>> # create a list of dictionaries
>>> allCats.append({'name': 'jacky', 'age': 7, 'color': 'gray'})
>>> allCats.append({'name': 'jane', 'age': 7, 'color': 'red'})
>>> allCats.append({'name': 'pooka', 'age': 17, 'color': 'black'})
>>> allCats.append({'name': '???', 'age': 17, 'color': 'orange'})
>>> allCats
[{'name': 'jacky', 'age': 7, 'color': 'gray'}, {'name': 'jane', 'age': 7, 'color': 'red'}, {'name': 'pooka', 'age': 17, 'color': 'black'}, {'name': '???', 'age': 17, 'color': 'orange'}]
>>> 
>>> 
>>> 
>>> 
>>> # a mini program: Tic Tac Toe
>>> theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
		'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
		'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
>>> import pprint
>>> pprint.pprint(theBoard)
{'low-L': ' ',
 'low-M': ' ',
 'low-R': ' ',
 'mid-L': ' ',
 'mid-M': ' ',
 'mid-R': ' ',
 'top-L': ' ',
 'top-M': ' ',
 'top-R': ' '}
>>> def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-----')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-----')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

	
>>> printBoard(theBoard)
 | | 
-----
 | | 
-----
 | | 
>>> 
>>> 
>>> # introduce type()
>>> type(42)
<class 'int'>
>>> type('str')
<class 'str'>
>>> type(theBoard)
<class 'dict'>
>>> type(theBoard['top-L'])
<class 'str'>
>>> 
