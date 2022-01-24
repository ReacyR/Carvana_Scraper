# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


def build_absolute_link(href):
    #build absolute link from the relative link scraped from page
    return f'https://www.carvana.com{href}'


class VehiclesItem(scrapy.Item):
    # define the fields for your item here like:

     Year = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
     Make = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
     Model = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
     Trim = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
     Miles = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
     Price = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
     Link = scrapy.Field(input_processor = MapCompose(remove_tags, build_absolute_link), output_processor = TakeFirst())
    
