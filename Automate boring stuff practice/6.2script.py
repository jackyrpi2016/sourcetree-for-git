
>>> # range objects and list-like values
>>> for i in range(4):
	print(i)

	
0
1
2
3
>>> # range(4) == range(0, 4)
>>> # we can also use list
>>> for i in [1, 2, 3, 4]:
	print(i)

	
1
2
3
4
>>> # transform range into list
>>> list(range(4))
[0, 1, 2, 3]
>>> # get some list from range, like [0, 2, 4]
>>> list(range(0, 10, 2))
[0, 2, 4, 6, 8]
>>> 
>>> 
>>> # use range and len to print a list
>>> supplies = ['pens', 'staplers', 'binders', 'ink']
>>> for i in range(len(supplies)):
	print('Index ' + str(i) + ' in supplies is ' + supplies[i])

	
Index 0 in supplies is pens
Index 1 in supplies is staplers
Index 2 in supplies is binders
Index 3 in supplies is ink
>>> 
>>> 
>>> 
>>> 
>>> # multiple assignment
>>> cat = ['fat', 'orange', 'loud']
>>> size, color, disposition = cat
>>> size
'fat'
>>> color
'orange'
>>> disposition
'loud'
>>> # another example of multiple assignment
>>> size, color, disposition = 'skinny', 'black', 'quiet'
>>> size
'skinny'
>>> color
'black'
>>> disposition
'quiet'
>>> 
>>> 
>>> # swapping variables
>>> a = 'AAA'
>>> b = 'BBB'
>>> a, b = b, a
>>> a
'BBB'
>>> b
'AAA'
>>> 
>>> 
>>> 
>>> 
>>> # augmented assignment operator
>>> # +=, -=, *=, /=, %/
>>> spam = 42
>>> spam += 1
>>> spam
43
>>> 
