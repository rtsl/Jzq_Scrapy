# -*- coding: utf-8 -*-

# Scrapy settings for Jzq_Scrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Jzq_Scrapy'

SPIDER_MODULES = ['Jzq_Scrapy.spiders']
NEWSPIDER_MODULE = 'Jzq_Scrapy.spiders'

DOWNLOAD_HANDLERS = {'s3':None,}

ITEM_PIPELINES={
    'Jzq_Scrapy.pipelines.JzqScrapyPipeline':300, 
}
LOG_LEVEL='DEBUG'

DOWNLOAD_DELAY = 2 
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'
COOKIES_ENABLED = True
MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'python'
MONGODB_COLLECTION = 'test'
