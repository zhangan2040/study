#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: anzhang28@163.com
# FileName: 51testinglogin.py
# login to the www.51testing.com

import basictest
import re


def get_imgsecode(html):
    # print('{0}'.format(html))
    pattern = re.compile('<img id="imgsecode" src="(.*?)".*?>')
    img_url = re.search(pattern, html).group(1)
    return img_url


def utf8_code(s, codec):
    return s.decode(codec).encode('utf-8')


class FoOpener(basictest.CookieOpener):
    def get_secode(self, html=None):
        if html is None:
            img_url = 'http://www.51testing.com/batch.seccode.php'
        else:
            img_url = get_imgsecode(html)
        if img_url is not None:
            try:
                img = self.opener.open(img_url)
                secode_img = open('secode.img', 'wb')
                secode_img.write(img.read())
                secode_img.flush()
                secode_img.close()
            except Exception, e:
                if hasattr(e, 'reason'):
                    print('Get secode occured a unexception error {0}'.format(e.reason))
            else:
                secode = raw_input('Please check the file secode.img, then input the secode:')
                return secode
        else:
            return None


if __name__ == '__main__':
    login_url = 'http://www.51testing.com/batch.login.php?action=login'
    referer = 'http://www.51testing.com/?action-login'
    name = raw_input('please input your username:')
    pw = raw_input('please input your password:')
    login_data = {
        'username': name,
        'password': pw,
        'cookietime': '0',
        'loginsubmit': 'true',
        'refer': 'http://www.51testing.com/?action-site-type-panel'
    }
    foopener = FoOpener(addheader=[('Referer', referer)])
    # login_res = foopener.post_data(login_url, login_data)
    # login_content = login_res.read()
    secode = foopener.get_secode()
    secode_data = {
        'seccode': secode,
        'securitysubmit': 'true',
        'uid': 'xxxxx',
        'password': 'xxxxxx',
        'cookietime': '0',
        'loginsubmit_secques': 'yes',
        'refer': 'http://www.51testing.com/?action-site-type-panel',
    }
    foopener.post_data(login_url, secode_data)
