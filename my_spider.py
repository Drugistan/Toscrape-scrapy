import scrapy
from ..items import QuotesItem
from scrapy.loader import  ItemLoader


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://quotes.toscrape.com',
    ]

    def parse(self, response):
        item_object = QuotesItem()
        for quote in response.css('div.quote'):
            item_loader = ItemLoader(item=QuotesItem(), selector=quote)
            item_loader.add_xpath('quotes', ".//span[@class='text']/text()")
            item_loader.add_xpath('author', ".//span/small/text()")
            tags = quote.xpath(".//div/a/text()")
            if tags:
                item_loader.add_xpath('tags', ".//div/a/text()")
            else:
                item_loader.add_value('tags', "No Tags Value")

            yield item_loader.load_item()
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
