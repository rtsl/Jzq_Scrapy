#!/usr/bin/env python
# coding=utf-8

from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
import scrapy.linkextractors.sgml as SG
from Jzq_Scrapy.items import JzqScrapyItem



class NetEaseSpider(CrawlSpider):
    name = "Jzq_Scrapy"
    allowed_domains = ["news.sina.com.cn"]
    start_urls = ["http://news.sina.com.cn"]
    rules = [
       # Rule(SG.SgmlLinkExtractor(allow=(r'http://news.sina.com.cn/[a-z]+/'))),
       # Rule(SG.SgmlLinkExtractor(allow=(r'http://news.sina.com.cn/[a-z]/[a-z]{2}/\d{4}-\d{2}-\d{2}/doc-ifxm[a-zA-Z0-9]+.shtml')),callback="parse_item"),
        Rule(SG.SgmlLinkExtractor(allow=(r'http://news.sina.com.cn/s/wh/2015-12-18/doc-ifxmttcn4968829.shtml')),callback="parse_item"),
        Rule(SG.SgmlLinkExtractor(allow=(r'http://news.sina.com.cn/c/nd/2015-12-18/doc-ifxmueaa3618078.shtml')),callback="parse_item"),
    ]
    def parse_item(self,response):
        sel_resp = Selector(response)
        news_item = JzqScrapyItem()
        news_item["news_type"]= sel_resp.xpath('//*[@id="wrapOuter"]/div/div[2]/div[1]/a/text()').extract()
        news_item["news_title"] = sel_resp.xpath('//*[@id="artibodyTitle"]/text()').extract()
        tmp = sel_resp.xpath('//*[@id="navtimeSource"]/text()').extract()
        news_item["news_date"] = tmp[0].split("\t")[0]
        news_item["news_source"] = sel_resp.xpath('//*[@id="navtimeSource"]/span/span/a/text()').extract()
        news_item["news_content"] = sel_resp.xpath('//*[@id="artibody"]/p/text()').extract()
        return news_item
