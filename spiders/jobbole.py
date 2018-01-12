#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anzhang28@163.com

import basictest


#class Jobbole(basictest.StaticPage):
#    def


if __name__ == '__main__':
    login_url = 'https://graph.qq.com/oauth2.0/authorize'
    login_data = {}
    login_data['response_type'] = 'code'
    login_data['client_id'] = 'xxxxx'
    login_data['redirect_uri'] = 'http://api.blogqun.com/authorize.php'
    login_data['scope'] = 'get_user_info,add_topic,add_one_blog,upload_pic,add_share,' \
                          'add_t,add_pic_t,get_info'
    login_data['state'] = ''
    login_data['switch'] = ''
    login_data['from_ptlogin'] = '1'
    login_data['src'] = '1'
    login_data['update_auth'] = '1'
    login_data['openapi'] = '80901010_80901020_2010_1040'
    login_data['g_tk'] = '144943610'
    login_data['auth_time'] = '1515747286057'
    login_data['ui'] = '96C782C5-CC69-48ED-AE80-7806B5A4B6C7'
    jobbole = basictest.StaticPage(login_url, data=login_data)
    login_res = jobbole.postData()
    print('{}'.format(login_res.code))
