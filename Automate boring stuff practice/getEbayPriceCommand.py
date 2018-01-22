# get current price from shopping webpage like Amazon or Ebay
# I cann't get any info about Amazon's webpage, for 503 error

#! /usr/bin/env python3

import bs4, requests, sys, pyperclip

def getEbayPrice(productURL):
    res = requests.get(productURL)
    # check the webpage accessibility
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elem = soup.select('#prcIsum')  # it applies to all the price tag
    return elem[0].text  # if elem has multiple elements, we should use .strip()

sys.argv # [getEbayPriceCommand.py, 'URL']

if len(sys.argv)>1:
    price = getEbayPrice(sys.argv[1])
else:
    price = getEbayPrice(pyperclip.paste())
print('The price is: ' + price)
