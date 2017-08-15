#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 13:59:18 2017

@author: maison
"""
import pandas as pd

#%%

# Make sure your working directory is the 
# /data-science-for-social-studies/jm  master folder.

#%%

metastr = ''

for x in range(2):
    with open('jm-search({}).txt'.format(str(x), 'r')) as file:
        print (x)
        content = file.read()
        splited_txt = content.split('http://www.journaldemontreal.com')
        search_len = len(splited_txt)
        l = []
        for y in range(search_len):
            l.append(' {}{}'.format('http://www.journaldemontreal.com',splited_txt[y][:splited_txt[y].find('">')]))
        metastr += ' '.join(list(set(l)))
        file.close()

ll = []
for x in range(len(list(set(metastr.split())))):
    if 'http://www.journaldemontreal.com/' in list(set(metastr.split()))[x]:
        ll.append(list(set(metastr.split()))[x])
    
        
        #%%
        
df = pd.DataFrame(index=range(len(ll)), columns = ['URL'], data=ll)
df.to_csv('url_list.csv')

