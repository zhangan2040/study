#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anzhang28@163.com
# FileName: bdtb.py
# function: get content-info form tieba.baidu.com
# date: 2017/01/10

import basictest
import re

alltag_re = re.compile('<.*?>')
br_re = re.compile('(?:<br>)+')
def removeTag(s):
    global alltag_re, br_re
    s = re.sub(br_re, '\n', s)
    s = re.sub(alltag_re, '', s)
    return s


class BdBrief:
    removeimg = re.compile('<img.*?>')
    removeat = re.compile('<a href=""\s+onclick.*?>')

    def __init__(self, content):
        self.content = content

    def replace(self):
        self.content = re.sub('[\r|\n]', '', self.content)
        self.content = re.sub(self.removeimg, '', self.content)
        self.content = re.sub(self.removeat, '', self.content)
        return self.content


class Bdtb(basictest.StaticPage):
    # 正则匹配的结果分别为层主名、内容、楼层数、发布时间
    fc_re = re.compile('<li class="icon">.*?<li class="d_name".*?>.*?<.*?>(.*?)<.*?>.*?<div id="post_' +
                       'content_.*?>(.*?)<div class="user-hide.*?>.*?<span class="tail-info">(\d+楼)' +
                       '</span>.*?<span.*?>(.*?)</span>')

    def __init__(self, url, lz=1):
        basictest.StaticPage.__init__(self, url)
        self.lz = lz
        self.mainpage = self.getArgsPage(see_lz=lz, pn=1).read()
    # 获取楼层内容
    def getFloorContent(self, pgcontent):
        bdbrief = BdBrief(pgcontent).replace()
        return self.fc_re.findall(bdbrief)
    # 获取页面数
    def getMaxPage(self):
        maxp_re = re.compile('<span\s+class="red">(\d+)</span>页')
        maxp = re.search(maxp_re, self.mainpage)
        return maxp.group(1)
    # 获取标题
    def getTitle(self):
        title_re = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>')
        title = re.search(title_re, self.mainpage)
        return title.group(1)
    # 写入帖子内容
    def writePageContent(self):
        title = self.getTitle()
        pgnum = self.getMaxPage()
        print('{}'.format(title))
        for n in range(1, int(pgnum) + 1):
            # BdBrief(self.getArgsPage(see_lz=self.lz, pn=n)).read().replace()
            cur_pg = self.getFloorContent(self.getArgsPage(see_lz=self.lz, pn=n).read())
            for c in cur_pg:
                print('floor: {2} time:{3} author: {0} \n {1}'.format(c[0], removeTag(c[1]).strip(), c[2], c[3]))


if __name__ == '__main__':
    bdtb = Bdtb('https://tieba.baidu.com/p/5233342442')
    bdtb.writePageContent()
