# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from db import db_methods as psql

# class ScraperPipeline:
#     def process_item(self, item, spider):
#         return item

class SaveToDatabasePipeline:
    def __init__(self):
        # Connect to the Postgres database and create the table if not yet created
        self.conn = psql.connect()
        self.create_table()

    def create_table(self):
        if not psql.table_exists(self.conn, "flat_listed"):
            psql.create_flat_listed_table(self.conn)
            self.conn.commit()

    def process_item(self, item, spider):
        psql.post_flat_listed(self.conn, str(item.title), str(item.image))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        ## Close cursor & connection to database 
        # self.cur.close()
        self.conn.close()