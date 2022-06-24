from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scraper.scraper.spiders.srealityspider import SrealitySpider
 
 
process = CrawlerProcess(get_project_settings())
process.crawl(SrealitySpider)
process.start()

print("Done crawling!")