#!/usr/bin/env python
# -*- coding:utf-8 -*-
# auhtor: anzhang28@163.com
# function: search the top n documentary film from douban

import urllib2
import re

class DoubanTop:
    def __init__(self, tag, top):
        self.url = 'https://movie.douban.com/tag/' + tag
        self.top = top
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
        }
    def getPageInfo(self, url):
        print('Get page from {}'.format(url))
        try:
            req = urllib2.Request(url, headers=self.header)
            res = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            print('HTTP error occured: {0} {1}'.format(e.code, e.reason))
            return False
        except urllib2.URLError, e:
            print('URL error occured: {}'.format(e.reason))
            return False
        else:
            return res
    def getTopFilm(self):
        start = 0
        type = 'T'
        film_re = re.compile('<a class="nbg" href="(.*?)"  title="(.*?)">')
        films = []
        while start < self.top:
            url = self.url + '?start=' + str(start) + '&type=' + type
            pageinfo = self.getPageInfo(url).read()
            if pageinfo:
                films += film_re.findall(pageinfo)
            start += 20
        return films

if __name__ == '__main__':
    n = 3
    top30 = DoubanTop('纪录片', n)
    films= top30.getTopFilm()
    i = 1
    for f in films:
        print('{0} {2} is located in {1}'.format(i, f[0], f[1]))
        if i >= n:
            break
        i += 1