import scrapy
from ..items import MaoyanSpidersItem
from scrapy.selector import Selector

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board']

    def parse(self, response):
        item = []
        item = MaoyanSpidersItem()
        movies = Selector(response=response).xpath('//div[@class="movie-item-info"]')
        for movie in movies:
            # item = MaoyanSpidersItem()
            item["name"] = movie.xpath('.//a/text()').extract_first().strip()
            item["star"] = movie.xpath('./p[@class="star"]/text()').extract_first().strip()
            item["releasetime"] = movie.xpath('./p[@class="releasetime"]/text()').extract_first().strip()
            yield item
            # name = movie.xpath('.//a/text()')
            # star = movie.xpath('./p[@class="star"]/text()')
            # releasetime = movie.xpath('./p[@class="releasetime"]/text()')
            # print(f'movie_info:{name.extract_first(),star.extract_first(),releasetime.extract_first()}')