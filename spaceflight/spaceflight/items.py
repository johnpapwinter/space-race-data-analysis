import scrapy


class SpaceflightItem(scrapy.Item):
    mission_name = scrapy.Field()
    organization = scrapy.Field()
    location = scrapy.Field()
    date = scrapy.Field()
    rocket_name = scrapy.Field()
    rocket_status = scrapy.Field()
    price = scrapy.Field()
    mission_status = scrapy.Field()
