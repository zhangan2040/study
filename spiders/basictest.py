#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auhtor: anzhang28@163.com
# FileName: basictest.py
# functions: some basic lib
# date: 2017/01/09

import urllib2
import re
import urllib
import cookielib

_UA = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
UA = _UA


class StaticPage:
    global _UA

    def __init__(self, url, data=None, useragent=_UA):
        self.url = url
        self.header = {
            'User-Agent': useragent
        }
        self.data = data

    def getPageInfo(self):
        print('Get content from '.format(self.url))
        try:
            req = urllib2.Request(self.url, headers=self.header)
            res = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            print('HTTP ERROR occured {0} {1}'.format(e.code, e.reason))
            return False
        except urllib2.URLError, e:
            print('URL ERROR occured {0}'.format(e.reason))
            return False
        except Exception, e:
            if hasattr(e, 'reason'):
                print('SPECIAL ERROR occured {0}'.format(e.reason))
            return False
        else:
            return res

    def getOnelineContent(self, content):
        return re.sub('[\r|\n]', '', content)

    def getArgsPage(self, **kwargs):
        try:
            args_list = []
            for item in kwargs.items():
                args_list.append(str(item[0]) + '=' + str(item[1]))
            if len(args_list) == 0:
                url = self.url
            else:
                url = self.url + '?' + '&'.join(args_list)
            req = urllib2.Request(url, headers=self.header)
            res = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            print('HTTP ERROR occured: {0} {1}'.format(e.code, e.reason))
            return False
        except urllib2.URLError, e:
            print('URL ERROR occured: {0}'.format(e.reason))
        else:
            return res

    def postData(self):
        if self.data is not None:
            try:
                pd = urllib.urlencode(self.data)
                req = urllib2.Request(self.url, data=pd, headers=self.header)
                res = urllib2.urlopen(req)
            except urllib2.HTTPError, e:
                print('Post data failed: {0} {1}'.format(e.code, e.reason))
                return False
            except urllib2.URLError, e:
                if hasattr(e, 'reason'):
                    print('Post data failed: {0}'.format(e.reason))
                return False
            else:
                return res
        else:
            raise Exception('Invalid Data', self.data)


class CookieOpener:
    def __init__(self, addheader=None):
        # create an OpenerDirector instance, which can handle cookie
        self.cookie = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        self.opener.addheaders = [
            ('User-Agent', UA)
        ]
        if addheader is not None:
            self.opener.addheaders += addheader

    def post_data(self, post_url, data=None):
        try:
            if data is not None:
                post_req = urllib2.Request(post_url, data=urllib.urlencode(data))
            else:
                post_req = urllib2.Request(post_url)
            post_res = self.opener.open(post_req)
        except 'Invalid Data':
            return None
        else:
            return post_res
