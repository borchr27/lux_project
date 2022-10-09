# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from PostgresDatabase import PostgresDatabase
import unidecode
from scrapy.exceptions import DropItem

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
        self.db.execute('INSERT INTO quotes (author, quote) VALUES (%s, %s)',
                        (
                            item['author'],
                            item['quote'],
                        ))
        self.db.commit()
        spider.logger.info('Processed item.')
        return item
    
    def close_spider(self, spider):
        spider.logger.info('Closing PostgresPipeline...')
        self.db.close()
        spider.logger.info('Closed PostgresPipeline.')


class ProcessingPipeline:
    
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if adapter.get('author'):
            author = adapter['author']
            adapter['author'] = unidecode.unidecode(author)
            
            if adapter.get('quote'):
                quote = str(adapter['quote']).replace('“',"").replace('”',"").replace("'","")
                adapter['quote'] = quote
                return item
        else:
            raise DropItem(f"Missing author or quote in {item}")