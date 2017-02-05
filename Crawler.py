# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 00:07:06 2017

@author: ktk
"""

import requests
from bs4 import BeautifulSoup
import lxml

res = requests.get("http://yanlong4869.blogspot.tw/2015/09/python-crawler.html")
soup = BeautifulSoup(res.text, 'lxml')
title = soup.select('h1')[0].text
content = soup.select('h4')[1].text                   
print title
print content