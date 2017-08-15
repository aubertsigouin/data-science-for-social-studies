#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 16:10:03 2017

@author: maison
"""
import urllib.request
import bs4 
import pandas as pd

#%%
url_list = []
for x in range(int(227/20)+1):
    url = 'https://www.thestar.com/search.html?q=idle%20no%20more&pagenum={}'.format((x*20)+1)
    url_list.append(url)
    
#%%
    
bs_object = str(bs4.BeautifulSoup(urllib.request.urlopen(url_list[1]).read(),'lxml'))
s = bs_object.split('"},"url":"')[1:]
for x in range(len(s)):
    s[x] = 'https://www.thestar.com{}.html'.format(s[x][:s[x].find('.html')])
    
#%%
    
