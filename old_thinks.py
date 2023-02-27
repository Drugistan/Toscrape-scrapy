# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QuotesPipeline:

    def __init__(self):
        self.cursor = None
        self.connection = None
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.connection = sqlite3.connect("./mydb.db")
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute\
                (
                            """ CREATE TABLE IF NOT EXISTS QUOTES_TABLE(Quotes Text, Author Text, Tags Text)"""
                )

    def process_item(self, item, spider):
        self.store_in_db(item)
        return item

    def store_in_db(self, item):
        self.cursor.execute(
            """INSERT OR IGNORE INTO QUOTES_TABLE Values(?, ?, ?)""",
            (
                str(item['quotes']),
                str(item['author']),
                str(item['tags'][0]))
        )

        self.connection.commit()

