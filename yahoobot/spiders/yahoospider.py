"""
This file holds the spider class for downloading some symbol data.
"""

import scrapy
from yahoobot.items import YahooSymbolItem
from bs4 import BeautifulSoup

class YahooSymbolsSpider(scrapy.Spider):
    """The spider class for downloading symbol data from yahoo finance UK."""

    # General settings
    name = "yahoosymbols"
    offset = 0
    jump = 20
    base_url = "https://uk.finance.yahoo.com/lookup/stocks?s=a&t=A&m=ALL&b="

    def start_requests(self):
        yield scrapy.Request(
            url=self.base_url + str(self.offset),
            callback=self.parse)

    def parse(self, response):
        # Get the div that holds all the other divs.
        symbol_divs = response.xpath(
            '//*[@id="lookup-page"]/section/div/div/div[1]/div/div').extract()

        if len(symbol_divs) > 0:
            # queue the next request.
            self.offset = self.offset + self.jump
            yield scrapy.Request(self.base_url + str(self.offset), callback=self.parse)

        # For each div grab some data.
        if len(symbol_divs) > 0:
            for div in symbol_divs[1:]:
                div_soup = BeautifulSoup(div, "lxml")

                spans = div_soup.find_all("span")

                symbol = spans[0].a.string
                company_name = spans[1].string
                last_price = spans[2].string
                industry_category = spans[3].string
                item_type = spans[4].string
                exchange = spans[5].string

                item = YahooSymbolItem(
                    symbol=symbol,
                    company_name=company_name,
                    last_price=last_price,
                    industry_category=industry_category,
                    item_type=item_type,
                    exchange=exchange)

                yield item
