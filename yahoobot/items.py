# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YahooSymbolItem(scrapy.Item):
    """A yahoo items, hold the ticker data."""
    symbol = scrapy.Field()
    company_name = scrapy.Field()
    last_price = scrapy.Field()
    industry_category = scrapy.Field()
    item_type = scrapy.Field()
    exchange = scrapy.Field()
