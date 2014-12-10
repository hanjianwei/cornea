# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib

import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline, NoimagesDrop


class PhotoImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['url'])

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise NoimagesDrop
        item['path'] = image_paths[0]

        return item

    def file_path(self, request, response=None, info=None):
        image_guid = hashlib.sha1(request.url).hexdigest()
        return 'full/%s.jpg' % image_guid
