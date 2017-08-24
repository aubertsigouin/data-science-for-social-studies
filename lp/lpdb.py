#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 18:28:08 2017

@author: aubert
"""

from newspaper import Article
import urllib.request
import bs4
import pandas
import numpy as np
import pandas

#%%
# """""""""""""""""""""
#    TIME ITERATOR
# """""""""""""""""""""

def time_iter(start,end,by): #by = D, W, M, Y, S
    return np.arange(start,end,dtype="datetime64[{}]".format(by))
    
arr_of_time = time_iter('2012-12-01','2013-07-01','D')
print(arr_of_time)


#%%
# """""""""""""""""""""
#   GET METAFOLDERS 

# """""""""""""""""""""

def get_url_links(journal, timerange):
    global timelist    
    urllist = []
    timelist = []
    for x in range(len(timerange)):
        timesplit = str(arr_of_time[x]).split('-')
        timelist.append(timesplit[0])
        month = timesplit[1]
        day = timesplit[2]
        if int(day) <= 9 and journal == 'lp':
            day = day [1:]
        if int(month) <= 9 and journal == 'lp':
            month = month [1:]
        timelist.append(month)
        timelist.append(day)
    if journal == 'lp':
        root_url = 'http://www.lapresse.ca/archives'
    newarr = np.array(timelist).reshape(len(timelist)/3,3)
    for y in range (len(newarr)):
        site = '{}/{}/{}/{}.php'.format(root_url,newarr[y][0],newarr[y][1],newarr[y][2])
        urllist.append(site)        
    return urllist

links = get_url_links(journal='lp',timerange=arr_of_time)
print('LINKS : {}'.format(links))

#%%
# """""""""""""""""""""
# GET URL LIST OF ALL
# SITES INSIDE A FOLDER 
# """""""""""""""""""""

def get_urls_inside_one_folder(url):
    req = urllib.request.Request(url = url, data=None, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
    f = str(bs4.BeautifulSoup(urllib.request.urlopen(req).read(),'lxml'))
    f = f[f.find('<div class="rail-left">'):f.find('</div> <!-- END .rail-left -->')].split('href="')
    l = []
    for x in range(len(f)):
        ff = f[x].split('title=')[0][:-2]
        l.append(ff)
    l=l[1:]

    return (l)
    
urls = get_urls_inside_one_folder(links[0])
print (urls)


#%%
# """"""""""""""""""""""""
# UNCOMMENT TO APPLY
# EXTRACTION TO ALL FOLDERS
# """"""""""""""""""""""""

#metalist = [] 
#for y in range(len(links)):
#        metalist.append(get_urls_inside_one_folder(links[y]))
#        print (y)
#print (metalist)        


#%%
# """""""""""""""""""""
# EXTRACT ARTICLE SITE
# FROM A LIST
# """""""""""""""""""""


site = {}
def get_articles(urls):
    global site
    global error_list 
    error_list = []
    for x in range(len(urls)):
#        try :
            url1 = urls[x]
            print ('|{}{}|'.format(int(x/len(urls)*10)*'-',(10-int(x/len(urls)*10))*' '))
            print('({}%)'.format(x/len(urls)*100))
            #while True:
            art = Article(url1, language='fr')
            print ('Downloading...')
            art.download()
            art.parse()
            print('Processing...')
            html = str(art.html)
            tag1 = html.find('|')
            tag2 = html.find('|',tag1+1)
            name = html[tag1+2:tag2-1]
            if '<' in name:
                name = 'NaN'
            if ',' in name:
                name = name[:name.find(',')]
                
            if art.text.startswith('('):
                city = art.text[art.text.find('(')+1:art.text.find(')')]
                art.text = art.text[art.text.find(')')+2:]
            else:
                city = 'NaN'     
            print('Appending')
            site1 = {'LEN_TXT' : len(art.text.split()), 'JOURNAL' : 'La Presse', 'CITY' : city,'URL': urls[x], 'TEXTE': art.text, 'TITRE' : art.title,'DATE' : '{}'.format(art.publish_date), 'AUTHORS' : name, 'META-KEYWORDS' : art.meta_keywords,'META-DESCRIPTION' : art.meta_description}
            site['ID {}-{}'.format(art.publish_date,x)]=site1
 #       except:
            error_list.append(url1)
            continue
    return(site)
    
    
#get_articles(urls)
#%%

df1 = pandas.DataFrame(get_articles(urls)).transpose()

#%%
#df1.to_csv('db')
#print (error_list)