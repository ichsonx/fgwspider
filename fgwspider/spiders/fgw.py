import scrapy
from selenium import webdriver
import time
import re
import json
import os
import datetime

class spider1024(scrapy.Spider):
    name = "fgw"
    # custom_settings = {
    #     'ITEM_PIPELINES': {
    #         'fgwspider.pipelines.FgwspiderPipeline':400
    #     }
    # }

    start_urls = ['http://www.szpb.gov.cn/xxgk/qt/tzgg/']

    for i in range(1, 2):
        start_urls.append('http://www.szpb.gov.cn/xxgk/qt/tzgg/index_'+ str(i) +'.htm')

    def __init__(self, *args, **kwargs):
        pass

    def parse(self, response):
        print(response.body)