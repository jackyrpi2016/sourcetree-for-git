# get current price from shopping webpage like Amazon or Ebay
# I cann't get any info about Amazon's webpage, for 503 error

import bs4, requests, sys

def getEbayPrice(productURL):
    res = requests.get(productURL)
    # check the webpage accessibility
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elem = soup.select('#prcIsum')  # it applies to all the price tag
    return elem[0].text  # if elem has multiple elements, we should use .strip()

price = getEbayPrice('https://www.ebay.com/itm/GoPro-HERO5-Black-12-MP-Waterproof-4K-Camera-Camcorder-Wi-Fi/332430123230?_trkparms=aid%3D222007%26algo%3DSIM.MBE%26ao%3D2%26asc%3D49007%26meid%3D995be17f29924472907a97e26f154b2e%26pid%3D100623%26rk%3D2%26rkt%3D6%26sd%3D122775065002&_trksid=p2047675.c100623.m-1')
print('The price is: ' + price)
