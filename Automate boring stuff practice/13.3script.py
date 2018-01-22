>>> # install beautifulsoap4 before parsing HTML
>>> import bs4
>>> import requests

>>> # attach to the webpage
>>> res = requests.get('https://www.ebay.com/itm/GoPro-HERO5-Action-Camera-Black-Edition-4K-HD-12MP-Waterproof-WIFI/122775065002?epid=230153482&hash=item1c95f6d1aa:g:hp8AAOSwxIRZ8iUL')
>>> res.raise_for_status()
>>> res.status_code
200
>>> soup = bs4.BeautifulSoup(res.text)

Warning (from warnings module):
  File "/usr/local/lib/python3.6/site-packages/bs4/__init__.py", line 181
    markup_type=markup_type))
UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 1 of the file <string>. To get rid of this warning, change code that looks like this:

 BeautifulSoup(YOUR_MARKUP})

to this:

 BeautifulSoup(YOUR_MARKUP, "lxml")

>>> # warning is not exception, remind you about HTML parser
>>> # hide this
>>> soup = bs4.BeautifulSoup(res.text, 'html.parser')
>>> elem = soup.select('#prcIsum')
>>> elem[0]
<span class="notranslate" content="325.0" id="prcIsum" itemprop="price" style="">US $325.00</span>
>>> elem[0].text
'US $325.00'
>>> 
