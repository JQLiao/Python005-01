import scrapy
from ..items import MaoyanSpidersItem
from scrapy.selector import Selector
import time

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/50']

    def start_requests(self):
        for i in range(0, 5):
            url = f'https://maoyan.com/board/50?offset={i*10}'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = MaoyanSpidersItem()
        movies = Selector(response=response).xpath('//div[@class="movie-item-info"]')
        for movie in movies:
            try:
                item["name"] = movie.xpath('.//a/text()').extract_first().strip()
                item["star"] = movie.xpath('./p[@class="star"]/text()').extract_first().strip().split('：')[1]
                item["releasetime"] = movie.xpath('./p[@class="releasetime"]/text()').extract_first().strip().split('：')[1]
                item['created_at'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                yield item
            except Exception as e:
                print(f'name:{item["name"]},error_info:{e}')

