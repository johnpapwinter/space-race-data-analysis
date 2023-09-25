import scrapy
from spaceflight.spaceflight.items import SpaceflightItem


class NextspaceflightSpider(scrapy.Spider):
    name = "nextspaceflight"
    allowed_domains = ["nextspaceflight.com"]
    start_urls = ["https://nextspaceflight.com/launches/past/?page=1"]

    def parse(self, response):
        launches = response.css('div.mdl-grid div.mdl-cell.mdl-cell--6-col')

        for launch in launches:
            yield from self.parse_launch(launch)

    def parse_launch(self, response):
        launch_item = SpaceflightItem()
        launch_item['organization'] = response.css('div.launch div.mdl-card__title-text span::text').get()
        launch_item['location'] = None
        launch_item['date'] = None
        launch_item['detail'] = response.css('div.launch h5::text').get()
        launch_item['rocket_status'] = None
        launch_item['price'] = None
        launch_item['mission_status'] = None

        yield launch_item
