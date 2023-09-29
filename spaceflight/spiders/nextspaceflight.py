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

            yield response.follow(target_url, callback=self.parse_launch)

        next_page = response.css('div.mdl-tabs__panel.is-active span.step-links div button::attr(onclick)').get()
        if next_page is not None:
            next_page_url = next_page.replace('location.href = ', '').replace("'", "").strip()
            next_page_url = base_url + '/launches/past/' + next_page_url
            yield response.follow(next_page_url, callback=self.parse)

    def parse_launch(self, response):
        launch_item = SpaceflightItem()
        launch_item['mission_name'] = response.css('section div.mdl-cell div.mdl-card__supporting-text h4::text').get()
        launch_item['location'] = (
            response.xpath('//h3[text()="Location"]').xpath('following-sibling::section')[0].xpath('.//h4/text()').get())
        launch_item['date'] = (
            response.css('section div.mdl-cell div.mdl-card__supporting-text div.mdl-grid.a div.mdl-cell span::text').get())
        launch_item['rocket_name'] = (
            response.css('section header div.mdl-card__title div.rcorners div.mdl-card__title-text span::text').get())
        launch_item['organization'] = (
            response.css('section div.mdl-cell div.mdl-card__supporting-text div.mdl-grid.a div.mdl-cell--6-col-desktop::text')[0].get())
        launch_item['rocket_status'] = (
            response.css('section div.mdl-cell div.mdl-card__supporting-text div.mdl-grid.a div.mdl-cell--6-col-desktop::text')[1].get())
        launch_item['price'] = (
            response.css('section div.mdl-cell div.mdl-card__supporting-text div.mdl-grid.a div.mdl-cell--6-col-desktop::text')[2].get())
        launch_item['mission_status'] = response.css('section h6.rcorners.status span::text').get()

        yield launch_item
