>>> # send an email from Gmail
>>> import smtplib
>>> # connect mail server
>>> conn = smtplib.SMTP('smtp.gmail.com', 587)
>>> # gmail port 587
>>> type(conn)
<class 'smtplib.SMTP'>
>>> conn
<smtplib.SMTP object at 0x1039625c0>
>>> # build connection to the server
>>> conn.ehlo()
(250, b'smtp.gmail.com at your service, [2604:6000:fe43:a700:dc2d:77fe:dbfe:c418]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')
>>> # 250 means ok
>>> # do encrption before loging in
>>> # tls encription
>>> conn.starttls()
(220, b'2.0.0 Ready to start TLS')
>>> # log in using gmail application password
>>> conn.login('jackyly9992@gmail.com', 'yyoqeaucfgvlwfga')
(235, b'2.7.0 Accepted')
>>> # b'2.7.0 Accepted' is a bytes object not a string
>>> conn.sendmail('jackyly9992@gmail.com', 'jackyly9992@gmail.com', 'Subject: it is a test mail \n\n Dear Jane, \nI miss you \n Jacky')
{}
>>> # 'Subject: it is a test mail \n\n, the first \n ends the subject editing, the second \n ends header's editing.  {} email fails to send
>>> conn.quit()
(221, b'2.0.0 closing connection q37sm711998qtj.66 - gsmtp')
>>> 
