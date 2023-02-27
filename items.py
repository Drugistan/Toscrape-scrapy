# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from scrapy.loader.processors import (MapCompose, TakeFirst, Join)


def clean_quote(text):

    return find_quotes(text)


def find_quotes(text):

    if text.find('\"'):
        take_first = text.replace(text[0], "")
        return take_first


class QuotesItem(scrapy.Item):
    author = scrapy.Field(output_processor=TakeFirst())
    quotes = scrapy.Field(
        input_processor=MapCompose(clean_quote),
        output_processor=TakeFirst())
    tags = scrapy.Field(output_processor=Join(","))
