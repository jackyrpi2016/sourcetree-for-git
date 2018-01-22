>>> # raise exceptions and assert statement
>>> 24 / 0
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    24 / 0
ZeroDivisionError: division by zero
>>> 
>>> # raise your own exceptions
>>> raise Exception('This is the error message.')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    raise Exception('This is the error message.')
Exception: This is the error message.
>>> 
== RESTART: /Volumes/Extend/Automate boring stuff practice/debugPrintBox.py ==
**********
*        *
*        *
*        *
*        *
*        *
*        *
**********
>>> 
== RESTART: /Volumes/Extend/Automate boring stuff practice/debugPrintBox.py ==
********************
**        **
**        **
**        **
**        **
**        **
**        **
********************
>>> # we should avoid symbol is more than 2
>>> 
== RESTART: /Volumes/Extend/Automate boring stuff practice/debugPrintBox.py ==
Traceback (most recent call last):
  File "/Volumes/Extend/Automate boring stuff practice/debugPrintBox.py", line 19, in <module>
    boxPrint('**', 10, 8)
  File "/Volumes/Extend/Automate boring stuff practice/debugPrintBox.py", line 12, in boxPrint
    raise Exception('"symbol" needs to be a string of length 1')
Exception: "symbol" needs to be a string of length 1
>>> 
== RESTART: /Volumes/Extend/Automate boring stuff practice/debugPrintBox.py ==
*
*
>>> # we should avoid height and width smaller than 2
>>> 
== RESTART: /Volumes/Extend/Automate boring stuff practice/debugPrintBox.py ==
Traceback (most recent call last):
  File "/Volumes/Extend/Automate boring stuff practice/debugPrintBox.py", line 20, in <module>
    boxPrint('*', 1, 1)
  File "/Volumes/Extend/Automate boring stuff practice/debugPrintBox.py", line 14, in boxPrint
    raise Exception('"width" and "height" must be greater or equal to 2.')
Exception: "width" and "height" must be greater or equal to 2.
>>> 
>>> 
>>> # do not want exceptions to cause program to crash or fail, just save it to log
>>> import traceback
>>> try:
	raise Exception('This is the error message.')
except:
	errorFile = open('error_log.txt', 'a')
	errorFile.write(traceback.format_exc())
	errorFile.close()
	print('The traceback info was written in error_log.txt')

116
The traceback info was written in error_log.txt
>>> try:
	raise Exception('This is the error message.')
except:
	errorFile = open('error_log.txt', 'a')
	errorFile.write(traceback.format_exc())
	errorFile.close()
	print('The traceback info was written in error_log.txt')

116
The traceback info was written in error_log.txt
>>> # use append mode, to constantly add error logs
>>> 
>>> 
>>> # assert, sanity checks
>>> # False always fail
>>> assert False, 'This is the error message.'
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    assert False, 'This is the error message.'
AssertionError: This is the error message.
>>> 
 RESTART: /Volumes/Extend/Automate boring stuff practice/assertTrafficLights.py 
{'ns': 'green', 'ew': 'red'}
{'ns': 'yellow', 'ew': 'red'}
>>> 
 RESTART: /Volumes/Extend/Automate boring stuff practice/assertTrafficLights.py 
{'ns': 'green', 'ew': 'red'}
{'ns': 'yellow', 'ew': 'green'}
>>> # this is the bug, no red at both directions
>>> 
 RESTART: /Volumes/Extend/Automate boring stuff practice/assertTrafficLights.py 
{'ns': 'green', 'ew': 'red'}
Traceback (most recent call last):
  File "/Volumes/Extend/Automate boring stuff practice/assertTrafficLights.py", line 18, in <module>
    switchLights(market_2nd)
  File "/Volumes/Extend/Automate boring stuff practice/assertTrafficLights.py", line 15, in switchLights
    assert 'red' in intersection.values(), 'Neither light is red' + str(intersection)
AssertionError: Neither light is red{'ns': 'yellow', 'ew': 'green'}
>>> 
>>> # assert is a developer bug, it is sanity check
>>> 
