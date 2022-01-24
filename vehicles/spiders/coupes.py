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

            coupe_item.add_css('Year', '')
            coupe_item.add_css('Make', '')
            coupe_item.add_css('Model', '')
            coupe_item.add_css('Trim', '')
            coupe_item.add_css('Miles', '')
            coupe_item.add_css('Price', '')
            coupe_item.add_css('Link', 'a::attr(href)')
            yield coupe_item.load_item()


#last working shell command that got close to price
#rx('.//div[@class="result-tile"]/a/div[@class="tk-shell"]/div[@class="tk-frame middle-frame"]/div[@class="tk-pane middle-frame-pane"]').get()

