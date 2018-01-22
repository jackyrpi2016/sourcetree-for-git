>>> # install requests before using
>>> # download files from web
>>> import requests
>>> res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
>>> res.status_code
200
>>> # 200 means everything alright, 404 means no response
>>> 
>>> len(res.text)
174130
>>> print(res.text[:500])
ï»¿The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.org/license


Title: Romeo and Juliet

Author: William Shakespeare

Posting Date: May 25, 2012 [EBook #1112]
Release Date: November, 1997  [Etext #1112]

Language: English


*** S
>>> # check if success
>>> # if fails, print exception
>>> 
>>> badRes = requests.get('https://automatetheboringstuff.com/files/sdfsfds.txt')
>>> badRes.status_code
404
>>> res.raise_for_status()
>>> badRes.raise_for_status()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    badRes.raise_for_status()
  File "/usr/local/lib/python3.6/site-packages/requests/models.py", line 935, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://automatetheboringstuff.com/files/sdfsfds.txt
>>> 
>>> 
>>> # save webpage on file
>>> # open with 'wb', to remain the unicode style
>>> # first create a .txt file in wb
>>> playFile = open('RomeoAndJuliet.txt', 'wb')
>>> for chunk in res.iter_content(100000):
	playFile.write(chunk)

100000
74130
>>> # iterates for 2 times, first write 100000 bytes, then write the rest of 74130 bytes

