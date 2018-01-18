>>> # logging, keep track the bugs
>>> import logging
>>> logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
>>> # a buggy factorial problem
>>> 1*2*3*4
24
>>> 1*2*3*4*5*6
720
>>> 
== RESTART: /Volumes/Extend/Automate boring stuff practice/logFactorial.py ==
0
>>> 
== RESTART: /Volumes/Extend/Automate boring stuff practice/logFactorial.py ==
2017-11-09 00:49:15,783 - DEBUG - Start of program
2017-11-09 00:49:15,823 - DEBUG - Start of factorial(5)
2017-11-09 00:49:15,857 - DEBUG - i is 0, total is 0
2017-11-09 00:49:15,890 - DEBUG - i is 1, total is 0
2017-11-09 00:49:15,923 - DEBUG - i is 2, total is 0
2017-11-09 00:49:15,957 - DEBUG - i is 3, total is 0
2017-11-09 00:49:15,991 - DEBUG - i is 4, total is 0
2017-11-09 00:49:16,022 - DEBUG - i is 5, total is 0
2017-11-09 00:49:16,056 - DEBUG - Return value is 0
0
2017-11-09 00:49:16,123 - DEBUG - End of program
>>> 
== RESTART: /Volumes/Extend/Automate boring stuff practice/logFactorial.py ==
2017-11-09 00:49:40,536 - DEBUG - Start of program
2017-11-09 00:49:40,552 - DEBUG - Start of factorial(5)
2017-11-09 00:49:40,602 - DEBUG - i is 1, total is 1
2017-11-09 00:49:40,656 - DEBUG - i is 2, total is 2
2017-11-09 00:49:40,704 - DEBUG - i is 3, total is 6
2017-11-09 00:49:40,754 - DEBUG - i is 4, total is 24
2017-11-09 00:49:40,803 - DEBUG - i is 5, total is 120
2017-11-09 00:49:40,855 - DEBUG - Return value is 120
120
2017-11-09 00:49:40,954 - DEBUG - End of program
>>> 
