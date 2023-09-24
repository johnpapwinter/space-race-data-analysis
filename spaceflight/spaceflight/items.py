import scrapy


class SpaceflightItem(scrapy.Item):
    organization = scrapy.Field()
    location = scrapy.Field()
    date = scrapy.Field()
    detail = scrapy.Field()
    rocket_status = scrapy.Field()
    price = scrapy.Field()
    mission_status = scrapy.Field()
