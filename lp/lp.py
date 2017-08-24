#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 12:49:55 2017

@author: maison
"""

import pandas as pd

#%%

# Make sure your working directory is the 
# /data-science-for-social-studies/lp  master folder.

#%%

metastr = ''

for x in range(10):
    with open('google-cse({}).txt'.format(str(x), 'r')) as file:
        print (x)
        content = file.read()
        splited_txt = content.split('http://www.lapresse.ca')
        search_len = len(splited_txt)
        l = []
        for y in range(search_len):
            l.append(' {}{}{}'.format('http://www.lapresse.ca',splited_txt[y][:splited_txt[y].find('.php')], '.php'))
        metastr += ' '.join(list(set(l)))
        file.close()
    
ll = []
for x in range(len(list(set(metastr.split())))):
    if 'http://www.lapresse.ca/' in list(set(metastr.split()))[x] and 'archive' not in list(set(metastr.split()))[x]:
        ll.append(list(set(metastr.split()))[x])
    
df = pd.DataFrame(index=range(len(ll)), columns = ['URL'], data=ll)
df.to_csv('url_list.csv')