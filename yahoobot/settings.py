# -*- coding: utf-8 -*-

# Scrapy settings for yahoobot project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import logging
BOT_NAME = 'yahoobot'

SPIDER_MODULES = ['yahoobot.spiders']
NEWSPIDER_MODULE = 'yahoobot.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'yahoobot (+https://yourname.co.uk) your@email.com'

# Logging
#LOG_LEVEL = logging.ERROR
#LOG_FILE = 'yahoobotlog.txt'

# Obey robots.txt rules, set to false as the API for the wiki is forbidden.
# It makes no sense that the API is forbidden!
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 128

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'wiktionarybot.pipelines.JsonWriterPipeline': 300,
#    'wiktionarybot.pipelines.RefinementPipeline': 200
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = False
# The initial download delay
AUTOTHROTTLE_START_DELAY = 3
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 10
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 4.0
