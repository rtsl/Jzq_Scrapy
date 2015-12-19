# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.exceptions import DropItem
from scrapy.conf import settings
import logging

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='/home/jzq/Documents/Jzq_Scrapy/Jzq_Scrapy/pipelines.log',
                filemode='w')

class JzqScrapyPipeline(object):

    def __init__(self):
            connection = pymongo.Connection(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
            db = connection[settings['MONGODB_DB']]
            self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
          if not data:
            valid = False
            raise DropItem("Missing %s of blogpost from %s" %(data, item['url']))
        if valid:
            new_moive=[{
                "news_type":item['news_type'],
                "news_date":item['news_date'],
                "news_title":item['news_title'],
                "news_source":item['news_source'],
                "news_content":item['news_content']
            }]
            self.collection.insert(new_moive)
            logging.info("Item wrote to MongoDB database %s/%s" % (settings['MONGODB_DB'], settings['MONGODB_COLLECTION'])) 
            logging.info("Item %s" % str(new_moive))
        return item

