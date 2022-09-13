import scrapy
from db import db_methods as psql

class SrealitySpider(scrapy.Spider):
    """! The main website scraping code. Please see the scrapy documentation for more details. https://docs.scrapy.org/en/latest/

    @param scrapy.Spider  Base class for scrapy spiders. All spiders must inherit from this class.
    """
    ## The name of the spider/crawler
    name = "sreality"
    ## The urls to scrape the information from 
    start_urls = ["https://www.whiskyshop.com/scotch-whisky/all?p=1","https://www.whiskyshop.com/scotch-whisky/all?p=2"]
    # start_urls = ["https://www.sreality.cz/en/search/for-sale/apartments?page=1"]
    # TODO use for loop to add additional pages to get 200 results

    def parse(self, response, **kwargs):
        """! A method that will be called to handle the response downloaded for each of the requests made. The response parameter is an instance of TextResponse that holds the page content and has further helpful methods to handle it.
        
        @param response  Upon receiving a response for each one, it instantiates Response objects and calls the callback method associated with the request (in this case, the parse method) passing the response as argument.
        
        @return  Returns none but scrapes the name and image from sites into the database
        """

        ## Connect to the Postgres database
        conn = psql.connect()
        psql.create_flat_listed_table(conn)
        conn.commit()
        
        for products in response.css('div.product-item-info'):
            try:
                ## Find the image in the html / soup
                image = products.css('img.product-image-photo').attrib['src']
            except:
                image = products.css('img.product-image-photo').attrib['data-original']
            
            ## Find the title in the html / soup 
            title = products.css('a.product-item-link::text').get()
            #image = products.css('img.product-image-photo').attrib['src']
            
            psql.post_flat_listed(conn, title, image)
            conn.commit()

            # yield {
            #     'title': products.css('a.product-item-link::text').get(),
            #     'image': image
            # }
        
        conn.close()
        # return super().parse(response, **kwargs)
        return None

# use CMD scrapy crawl sreality
# in the first /scraper folder to run the scraping 