import scrapy
from db import db_methods as psql

URL = 'https://www.whiskyshop.com/scotch-whisky/all'

class SrealitySpider(scrapy.Spider):
    name = "sreality"
    # start_urls = ["https://www.sreality.cz/en/search/for-sale/apartments?page=1"]
    # TODO use for loop to add additional pages to get 200 results
    
    
    def start_requests(self):
        yield scrapy.Request(URL, meta={'playwright': True})
        #return super().start_requests()

    def parse(self, response, **kwargs):
        conn = psql.connect()
        psql.create_flat_listed_table(conn)
        
        for products in response.css('div.product-item-info'):
            title = products.css('a.product-item-link::text').get()
            image = products.css('img.product-image-photo').attrib['src']
            psql.post_flat_listed(conn, title, image)

            # yield {
            #     'title': products.css('a.product-item-link::text').get(),
            #     'image': products.css('img.product-image-photo').attrib['src']
            # }
        conn.close()
        print(f"{URL} :: scraped successfully!")
        # return super().parse(response, **kwargs)

# use CMD scrapy crawl sreality
# in the first /scraper folder to run the scraping 