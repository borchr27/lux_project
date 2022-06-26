import scrapy
from db import db_methods as psql

URL = "https://www.whiskyshop.com/scotch-whisky/all"

class SrealitySpider(scrapy.Spider):
    name = "sreality"
    start_urls = [URL]
    # start_urls = ["https://www.sreality.cz/en/search/for-sale/apartments?page=1"]
    # TODO use for loop to add additional pages to get 200 results

    def parse(self, response, **kwargs):
        conn = psql.connect()
        psql.create_flat_listed_table(conn)
        conn.commit()
        conn.close()
        
        for products in response.css('div.product-item-info'):
            try:
                image = products.css('img.product-image-photo').attrib['src']
            except:
                image = products.css('img.product-image-photo').attrib['data-original']

            title = products.css('a.product-item-link::text').get()
            #image = products.css('img.product-image-photo').attrib['src']
            
            conn = psql.connect()
            psql.post_flat_listed(conn, title, image)
            conn.commit()
            conn.close()

            # yield {
            #     'title': products.css('a.product-item-link::text').get(),
            #     'image': image
            # }
            
        # return super().parse(response, **kwargs)
        return None

# use CMD scrapy crawl sreality
# in the first /scraper folder to run the scraping 