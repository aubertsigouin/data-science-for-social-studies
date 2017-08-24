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
metastr= ''
new_l = []

for y in range(len(url_list)):
    bs_object = str(bs4.BeautifulSoup(urllib.request.urlopen(url_list[y]).read(),'lxml'))
    s = bs_object.split('.html')[1:]
    
    for x in range(len(s)):
        s[x] = s[x][s[x].rfind('href="/'):]
        if '/news/' in s[x] or '/trust/' in s[x] or '/life/' in s[x] or '/entertainment/' in s[x] or '/opinion/' in s[x] or '/sports/' in s[x] or '/business/' in s[x] or '/yourtoronto/' in s[x]:
            if s[x].count('/') >2:
                new_l.append(s[x])
                
uniques = list(set(new_l))
    
for x in range(len(uniques)):
    uniques[x] = 'https://www.thestar.com/{}.html'.format(uniques[x][uniques[x].find('/'):])

df = pd.DataFrame(index=range(len(uniques)), columns = ['URL'], data=uniques)
df.to_csv('url_list.csv')

#%%
    
