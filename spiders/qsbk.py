#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: anzhang28@163.com
# FileName: qsbk.py
# function: search story from qiushibaike
# date: 2017/01/09

import re
import basictest


class Qsbk(basictest.StaticPage):
    def getBriefContent(self):
        pginfo = self.getOnelineContent(self.getPageInfo().read())
        sc_re = re.compile('<div\s+class=.*?id=.*?><div\s+class="author clearfix">.*?<h2>(.*?)</h2>.*?' +
                           '</div>.*?<div class="content"><span>(.*?)</span>.*?<!-- 图片或gif -->(.*?)' +
                           '<div class="stats">.*?<span class="stats-vote"><i class="number">(\d+)</i>' +
                           '.*?<i class="number">(\d+)')
        sc = sc_re.findall(pginfo)
        return sc

    def getNoImgContent(self):
        nic = []
        sc = self.getBriefContent()
        for s in sc:
            if len(s[2]) == 0:
                nic.append(s)
        return nic

    def startPrintRocorder(self):
        sc = []
        pg = 1
        bsurl = self.url
        while pg:
            self.url = bsurl + str(pg)
            print('loading story form {0} ......'.format(self.url))
            sc += self.getNoImgContent()
            for s in sc:
                flag = raw_input("press any key to continue except Q/q to quit\n")
                if flag == 'q' or flag == 'Q':
                    break
                else:
                    print('author:{0}\n{1}\nAN: {2} QN:{3}'
                          .format(s[0], re.sub('(<br/>)', '\n', s[1]), s[3], s[4]))
            nextpg = raw_input('Press Y/y to continue scanning next page')
            if nextpg == 'y' or nextpg == 'Y':
                sc = []
                pg += 1
            else:
                break


if __name__ == '__main__':
    qsbk = Qsbk('https://www.qiushibaike.com/hot/page/')
    qsbk.startPrintRocorder()
