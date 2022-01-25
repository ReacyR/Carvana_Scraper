import scrapy
from vehicles.items import VehiclesItem
from scrapy.loader import ItemLoader


class CoupesSpider(scrapy.Spider):
    name = 'coupes'
    allowed_domains = ['www.carvana.com/']
    start_urls = ['https://www.carvana.com/cars/coupe/']

    def parse(self, response):

        #parse the details of each result on the page and hand them off to the items pipeline for cleaning


        for result in response.css('.result-tile'):
            coupe_item = ItemLoader(item= VehiclesItem(), selector= result)

            coupe_item.add_css('Year', '.year-make-experiment', re='\d+')
            coupe_item.add_css('Make', '.year-make-experiment')
            coupe_item.add_css('Model', '.year-make-experiment')
            coupe_item.add_css('Trim', '.trim-mileage')
            coupe_item.add_css('Miles', '.trim-mileage', re='\d+,\d+')
            coupe_item.add_css('Price', 'div.price-variant')

            coupe_item.add_css('Link', 'a::attr(href)')
            yield coupe_item.load_item()


