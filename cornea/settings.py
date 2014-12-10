# -*- coding: utf-8 -*-

# Scrapy settings for cornea project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'cornea'

SPIDER_MODULES = ['cornea.spiders']
NEWSPIDER_MODULE = 'cornea.spiders'

ITEM_PIPELINES = {
    'cornea.pipelines.PhotoImagePipeline': 800,
}

IMAGES_STORE = '/Users/hjw/images'

COOKIES_ENABLED = False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cornea (+http://www.yourdomain.com)'
