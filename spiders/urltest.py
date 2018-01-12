#!/usr/bin/env python
# -*- coding:utf-8 -*-
# auhtor: anzhang28@163.com

import urllib2
from bs4 import BeautifulSoup
import cookielib
import re

if __name__ == '__main__':
    url = 'https://movie.douban.com/tag/%E7%BA%AA%E5%BD%95%E7%89%87?start=0&type=T'
    req = urllib2.Request(url)
    try:
        res = urllib2.urlopen(req)
    except urllib2.HTTPError,e:
        print('Error occured: {} {}'.format(e.code, e.reason))
    except urllib2.URLError, e:
        print('Error occured: {}'.format(e.reason))
    #finally:
    #     res = ''
    else:
        soup = BeautifulSoup(res, 'lxml')
        n = 0
        for s in soup.select('name'):
            n += 1
            print(s)
            print('client number is {}'.format(n))

    #cookie-store test start
    #create a file to strore the baidu cookie
    #filename = '51testing.txt'
    #cookie = cookielib.MozillaCookieJar(filename) #store cookie in a file
    #cookie = cookielib.CookieJar() #store cookie in a varable var
    #handler = urllib2.HTTPCookieProcessor(cookie)
    #opener = urllib2.build_opener(handler)
    #res = opener.open('http://www.51testing.com/html/index.html')
    #for item in cookie:
    #    print('name is {0} value is {1}'.format(item.name, item.value))
    #cookie.save(ignore_discard = True, ignore_expires = True)
    #cookie-store test end

    #cookie-load test start
    #cookie = cookielib.MozillaCookieJar()
    #cookie.load('baidu.txt', ignore_discard = True, ignore_expires = True)
    #req = urllib2.Request(url)
    #handler = urllib2.HTTPCookieProcessor(cookie)
    #opener = urllib2.build_opener(handler)
    #res = opener.open(req)
    #print(res.read())
    #cookie-load test end