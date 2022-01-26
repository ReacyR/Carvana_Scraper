# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags
import re


def build_absolute_link(href):
    #build absolute link from the relative link scraped from page
    return f'https://www.carvana.com{href}'


def get_trim(trim_mileage):
    #extract the trim from the tag that has has both trim & mileage
    
    trim = re.search(r'.*(?=\s\u2022)', trim_mileage)
    trim = trim.group(0)

    return trim


def get_make(year_make_model):
    #extract the make from the tag that has year, make, & model
    make = re.search(r'(?<=\d{4}).*', year_make_model)
    make = make.group(0).strip().split(' ')
    return make[0]



def get_model(year_make_model):
    #extract the model from the tag that has year, make, & model
    model = re.search(r'(?<=\d{4}).*', year_make_model)
    model = model.group(0).strip().split(' ')
    model = ",".join(model[1:]).replace(',', ' ')
    return model



class VehiclesItem(scrapy.Item):
    # define the fields for your item here like:

     Year = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
     Make = scrapy.Field(input_processor = MapCompose(remove_tags, get_make), output_processor = TakeFirst())
     Model = scrapy.Field(input_processor = MapCompose(remove_tags, get_model), output_processor = TakeFirst())
     Trim = scrapy.Field(input_processor = MapCompose(remove_tags, get_trim), output_processor = TakeFirst())
     Miles = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
     Price = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
     Link = scrapy.Field(input_processor = MapCompose(remove_tags, build_absolute_link), output_processor = TakeFirst())
    
