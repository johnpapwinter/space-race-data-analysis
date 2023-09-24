import scrapy


class NextspaceflightSpider(scrapy.Spider):
    name = "nextspaceflight"
    allowed_domains = ["nextspaceflight.com"]
    start_urls = ["https://nextspaceflight.com/launches/past/?page=1"]

    def parse(self, response):
        pass
