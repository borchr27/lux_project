# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from PostgresDatabase import PostgresDatabase
from scrapy.exceptions import DropItem
from bs4 import BeautifulSoup
import re

class DatabasePipeline():
    def __init__(self):
        # Connect to the Postgres database and create the table if not yet created
        self.db = PostgresDatabase()

    def open_spider(self, spider):
        spider.logger.info(f'Opening DatabasePipeline')
        # spider.logger.info(f'Opening PostgresPipeline on {os.environ["POSTGRES_HOST"]}:{os.environ["POSTGRES_PORT"]}...')
        self.db.connect()
        # self.db.execute('CREATE TABLE IF NOT EXISTS quotes (id serial not null, author text not null, quote text not null);')
        spider.logger.info('Opened DatabasePipeline.')

    def process_item(self, item, spider):
        spider.logger.info('Processing item...')
        
        # Check if the title already exists in the database
        self.db.execute('SELECT COUNT(*) FROM sites WHERE title = %s', (item['title'],))
        result = self.db.cursor.fetchone()
        count = result[0]
        
        if count == 0:  # Title doesn't exist, insert it
            self.db.execute('INSERT INTO sites (title, info) VALUES (%s, %s)',
                            (
                                item['title'],
                                item['info'],
                            ))
            self.db.commit()
            spider.logger.info('Title added to the database.')
        else:
            spider.logger.info('Title already exists in the database.')

        spider.logger.info('Processed item.')
        return item

    
    def close_spider(self, spider):
        spider.logger.info('Closing PostgresPipeline...')
        self.db.close()
        spider.logger.info('Closed PostgresPipeline.')


class ProcessingPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if adapter.get('info'):
            html = adapter['info']
            soup = BeautifulSoup(html , 'html.parser')
            text = soup.get_text()  # get text from html
            text = " ".join(text.split()) # remove extra spaces
            spider.logger.info(f'Processing item: {text}')
            adapter['info'] = text

            if adapter.get('title'):
                url_string = str(adapter['title'])  # previously called name
                pattern = r"https?://(www\.)?([^/?]+)"
                match = re.match(pattern, url_string)
                website_name = match.group(2)
                adapter['title'] = website_name
                return item            
        else:
            raise DropItem(f"Missing website data at: {item}")