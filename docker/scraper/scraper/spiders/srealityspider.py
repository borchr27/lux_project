import json
from math import ceil
import scrapy
from scraper.items import ScraperItem

class SrealitySpider(scrapy.Spider):
    """! The main website scraping code. Please see the scrapy documentation for more details. https://docs.scrapy.org/en/latest/

    @param scrapy.Spider  Base class for scrapy spiders. All spiders must inherit from this class.
    """
    ## The name of the spider/crawler
    name = "sreality"
    allowed_domains = ['sreality.cz']
    page = 1
    start_urls = ['https://www.sreality.cz/api/en/v2/estates?category_main_cb=2&category_type_cb=1&page=1&per_page=20']

    def parse(self, response, **kwargs):
        """! A method that will be called to handle the response downloaded for each of the requests made. The response parameter is an instance of TextResponse that holds the page content and has further helpful methods to handle it.
        
        @param response  Upon receiving a response for each one, it instantiates Response objects and calls the callback method associated with the request (in this case, the parse method) passing the response as argument.
        
        @return  Returns none but scrapes the name and image from sites into the database
        """
        
        # Load json response in and extract data 
        json_load = json.loads(response.text)
        data = json_load['_embedded']['estates']
        results_count = int(json_load['result_size'])
        
        item = ScraperItem()

        for x in data:
            item['title'] = x['name']
            item['image'] = x['_links']['images'][0]['href']
            yield item

        # Scrape additional pages up to 200 entries
        if (results_count > 200 and self.page < 10) or (results_count < 200 and self.page <= ceil(results_count/20)):
            self.page += 1
            url = f"https://www.sreality.cz/api/en/v2/estates?category_main_cb=2&category_type_cb={self.page}&page=1&per_page=20"
            yield scrapy.Request(url=url, callback=self.parse)
    
        # conn.close()
        # return super().parse(response, **kwargs)
        # return None

# use CMD scrapy crawl sreality
# in the first /scraper folder to run the scraping 