# -*- coding:utf-8 -*-
import requests
from lxml import etree
import os

start_urls = ['http://www.szpb.gov.cn/xxgk/qt/tzgg/index.htm']
for i in range(1, 41):
    start_urls.append('http://www.szpb.gov.cn/xxgk/qt/tzgg/index_' + str(i) + '.htm')

for url in start_urls:
    print(url)
    page_req = requests.get(url)
    html = page_req.text.encode('iso-8859-1').decode('gbk')
    selector = etree.HTML(html, parser=None, base_url=None)
    contents = selector.xpath('//span[contains(text(), "节能")][contains(text(), "2015")][contains(text(), "项目公示")][contains(@class, "p_bt")]/../@href')
    # if os.path.isfile('result.txt'):
    #     os.remove("result.txt")
    for text in contents:
        with open("result.txt", "a") as file :
            link = 'http://www.szpb.gov.cn/xxgk/qt/tzgg/' + text.replace("./", "")
            file.write(link + '\n')