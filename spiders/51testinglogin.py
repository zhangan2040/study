#!/usr/bin/env python
# -*- coding:utf-8 -*-
# auhtor: anzhang28@163.com
# FileName: 51testinglogin.py
# login to the www.51testing.com

import basictest


class FoTest(basictest.StaticPage):
    def login(self):
        try:
            res = self.postData()
        except 'Invalid Data':
            return False
        else:
            return res


if __name__ == '__main__':
    url = 'http://www.51testing.com/batch.login.php?action=login'
    referer = 'http://www.51testing.com/?action-login'
    name = raw_input('please input your username:')
    pw = raw_input('please input your password:')
    postdata = {
        'username': name,
        'password': pw,
        'cookietime': '0',
        'loginsubmit': 'true',
        'refer': 'http://www.51testing.com/?action-site-type-panel'
    }
    fotest = FoTest(url, data=postdata)
    fotest.header.update({'Referer': referer})
    login_res = fotest.login()
    if login_res:
        print('{}'.format(login_res.read().decode('gbk').encode('utf-8')))
