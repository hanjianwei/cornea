import arrow
from math import ceil
import scrapy

from cornea.items import PhotoItem


class BaiduImageSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['image.baidu.com']
    start_urls = []

    def __init__(self, **kwargs):
        self.word = kwargs.pop('word', 'image')
        count = kwargs.pop('count', 10000)

        for i in xrange(int(ceil(count / 20.0))):
            url = 'http://image.baidu.com/i?z=0&fr=&cl=2&ct=201326592&lm=-1&rn=20&tn=baiduimagenojs&s=0&' \
                  'word={word}&ie=utf-8&pn={start}'.format(word=self.word, start=i*20)
            self.start_urls.append(url)

        super(BaiduImageSpider, self).__init__(**kwargs)

    def parse(self, response):
        for url in response.xpath('//td/a/@href').re(r'objurl=(.*)'):
            item = PhotoItem()
            item['url'] = url
            item['keyword'] = self.word
            item['downloaded_at'] = arrow.utcnow().isoformat()

            yield item

