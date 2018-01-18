>>> # log in, fill forms or click buttons
>>> from selenium import webdriver
>>> browser = webdriver.Firefox()
>>> browser.get('https://automatetheboringstuff.com')
>>> 
>>> # click on a link, Copy Css selector
>>> # use something similar to BeautifulSoap's select()
>>> elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(18) > li:nth-child(2) > a:nth-child(1)')
>>> elem.click()
>>> 
>>> # get all paragraph elements
>>> elems = browser.find_element_by_css_selector('p')
>>> len(elems)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    len(elems)
TypeError: object of type 'FirefoxWebElement' has no len()
>>> elems = browser.find_elements_by_css_selector('p')
>>> len(elems)
218
>>> 
>>> # type text in a searchbox
>>> browser.get('https://www.ebay.com')
>>> searchElem = browser.find_element_by_css_selector('#gh-ac')
>>> searchElem.send_keys('gopro5')
>>> searchElem.submit()
>>> 
>>> # direct control over browser
>>> browser.back()
>>> browser.forward()
>>> browser.refresh()
>>> browser.quit()
>>> 
>>> # read the text
>>> browser = webdriver.Firefox()
>>> browser.get('https://automatetheboringstuff.com')
>>> elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > p:nth-child(7)')
>>> elem.text
"In Automate the Boring Stuff with Python, you'll learn how to use Python to write programs that do in minutes what would take you hours to do by hand-no prior programming experience required. Once you've mastered the basics of programming, you'll create Python programs that effortlessly perform useful and impressive feats of automation to:"
>>> 
>>> # get entire text of the website
>>> elem = browser.find_element_by_css_selector('html')
>>> elem.text
"Home | Buy on No Starch Press | Buy on Amazon | @AlSweigart |\nAutomate the Boring Stuff with Python\nPractical programming for total beginners. Written by Al Sweigart.\nFree to read under a Creative Commons license.\n\nLearn to Code\nIf you've ever spent hours renaming files or updating hundreds of spreadsheet cells, you know how tedious tasks like these can be. But what if you could have your computer do them for you?\nIn Automate the Boring Stuff with Python, you'll learn how to use Python to write programs that do in minutes what would take you hours to do by hand-no prior programming experience required. Once you've mastered the basics of programming, you'll create Python programs that effortlessly perform useful and impressive feats of automation to:\nSearch for text in a file or across multiple files\nCreate, update, move, and rename files and folders\nSearch the Web and download online content\nUpdate and format data in Excel spreadsheets of any size\nSplit, merge, watermark, and encrypt PDFs\nSend reminder emails and text notifications\nFill out online forms\nStep-by-step instructions walk you through each program, and practice projects at the end of each chapter challenge you to improve those programs and use your newfound skills to automate similar tasks.\nDon't spend your time doing work a well-trained monkey could do. Even if you've never written a line of code, you can make your computer do the grunt work. Learn how in Automate the Boring Stuff with Python.\nUdemy Online Video Course\nThe Automate the Boring Stuff with Python Programming online course on Udemy.com covers most of the content of the book. If you'd prefer a video format for learning to program, you can use the discount code FOR_LIKE_10_BUCKS to get an 80% discount. You will have lifetime access to the course content and can post questions to the course's forums.\nTable of Contents\nChapter 0 – Introduction\nChapter 1 – Python Basics\nChapter 2 – Flow Control\nChapter 3 – Functions\nChapter 4 – Lists\nChapter 5 – Dictionaries and Structuring Data\nChapter 6 – Manipulating Strings\nChapter 7 – Pattern Matching with Regular Expressions\nChapter 8 – Reading and Writing Files\nChapter 9 – Organizing Files\nChapter 10 – Debugging\nChapter 11 – Web Scraping\nChapter 12 – Working with Excel Spreadsheets\nChapter 13 – Working with PDF and Word Documents\nChapter 14 – Working with CSV Files and JSON Data\nChapter 15 – Keeping Time, Scheduling Tasks, and Launching Programs\nChapter 16 – Sending Email and Text Messages\nChapter 17 – Manipulating Images\nChapter 18 – Controlling the Keyboard and Mouse with GUI Automation\nAppendix A – Installing Third-Party Modules\nAppendix B – Running Programs\nAppendix C – Answers to the Practice Questions\nAdditional Content\nDownload files used in the book\nList of CSS Selector Tutorials\nList of JSON APIs\nList of Programming Practice Sites\nList of Web Comics\nSchedulers for Windows, Mac, and Linux\nHow to Do PyCon (or any tech conference)\nAbout the Author\nAl Sweigart is a software developer and teaches programming to kids and adults. He has written several books for beginners, including Scratch Programming Playground, Hacking Secret Ciphers with Python, Invent Your Own Computer Games with Python, and Making Games with Python & Pygame\nSupport the author by purchasing the print & ebook bundle from No Starch Press or separately on Amazon.\nRead the author's other Creative Commons licensed Python books."
>>> 
