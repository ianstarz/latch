import scrapy
import time
from concertScraper.items import ConcertScraperItem


class OgdenSpider(scrapy.Spider):
    name = "ogden"
    allowed_domains = ["ogdentheatre.com"]
    start_urls = ["http://www.ogdentheatre.com/events"]

    def parse(self, response):
        for sel in response.css("#eventsList").xpath('div'):
            item = ConcertScraperItem()
            item['headliner'] = sel.xpath('div/div/h3/a/text()').extract()
            item['date'] = sel.xpath('div/div/span[@class="date"]/text()')[1].extract().strip()
            item['concert_time'] = sel.xpath('div/div/span[@class="time"]/text()')[1].re("\d:\d+\s\w+")[0]
            yield item
