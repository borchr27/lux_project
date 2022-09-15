# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from db import db_methods as psql
import unidecode
from scrapy.exceptions import DropItem

class DatabasePipeline(object):
    def __init__(self):
        # Connect to the Postgres database and create the table if not yet created
        self.conn = psql.connect()
        psql.create_flat_listed_table(self.conn)

    def process_item(self, item, spider):
        psql.post_flat_listed(self.conn, item)
        self.conn.commit()
        return item
    
    def close_spider(self, spider):
        ## Close cursor & connection to database 
        # self.cur.close()
        self.conn.close()


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