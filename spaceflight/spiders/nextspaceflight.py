import scrapy
from spaceflight.items import SpaceflightItem


class NextspaceflightSpider(scrapy.Spider):
    name = "nextspaceflight"
    allowed_domains = ["nextspaceflight.com"]
    start_urls = ["https://nextspaceflight.com/launches/past/?page=1"]

    def parse(self, response):
        launches = response.css('div.mdl-grid div.mdl-cell.mdl-cell--6-col')
        base_url = 'https://nextspaceflight.com'

        for launch in launches:
            target_url = launch.css('div.launch div.mdl-card__actions div button.mdc-button::attr(onclick)').get()
            target_url = target_url.replace('location.href = ', '').replace("'", "").strip()
            target_url = base_url + target_url

            # yield print(f"This is the URL: {target_url}")
            yield response.follow(target_url, callback=self.parse_launch)

    def parse_launch(self, response):
        launch_item = SpaceflightItem()
        launch_item['mission_name'] = response.css('section div.mdl-cell div.mdl-card__supporting-text h4::text').get()
        launch_item['organization'] = (
            response.css('section div.mdl-cell div.mdl-card__supporting-text div.mdl-grid.a div.mdl-cell--6-col-desktop::text')[0].get())
        launch_item['location'] = (
            response.css('section.card div.mdl-card__supporting-text h4.mdl-card__title-text::text')[2].get())
        launch_item['date'] = (
            response.css('section div.mdl-cell div.mdl-card__supporting-text div.mdl-grid.a div.mdl-cell span::text').get())
        launch_item['rocket_name'] = (
            response.css('section header div.mdl-card__title div.rcorners div.mdl-card__title-text span::text').get()) # CLEAN
        launch_item['rocket_status'] = (
            response.css('section div.mdl-cell div.mdl-card__supporting-text div.mdl-grid.a div.mdl-cell--6-col-desktop::text')[1].get()) # CLEAN
        launch_item['price'] = (
            response.css('section div.mdl-cell div.mdl-card__supporting-text div.mdl-grid.a div.mdl-cell--6-col-desktop::text')[2].get()) # CLEAN
        launch_item['mission_status'] = response.css('section h6.rcorners.status span::text').get()

        yield launch_item
