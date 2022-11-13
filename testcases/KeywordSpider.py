# -*- coding: utf-8 -*-
# @Author     : Bonnie
# @Time       : 2022/10/30 22:02
# @FileName   : KeywordSpider.py
# @Description:
import scrapy

class KeywordSpider(scrapy.Spider):
    name = 'test'
    start_urls = ['http://www.tcpjwtester.top/personal_information']

    def parse(self, response):
        print(str(response.body,encoding="utf-8"))
        # result_list = response.xpath("//*[@id='menu']/following-sibling::table/tbody/tr[2]/@onclick")
        # print(result_list)
