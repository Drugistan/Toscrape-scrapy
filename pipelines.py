# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface


from .models import db_connect, create_table, Quote
from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem


class QuotesPipeline:

    def __init__(self):
        self.engine = db_connect()
        create_table(self.engine)
        self.session = sessionmaker(bind=self.engine)

    def process_item(self, item, spider):
        session = self.session()
        quote = Quote()
        quote.Quote = str(item['quotes'])
        quote.Author = str(item['author'])
        quote.Tags = str(item['tags'])

        try:
            session.add(quote)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return item


class DuplicatePipeline:

    def __init__(self):
        self.engine = db_connect()
        create_table(self.engine)
        self.session = sessionmaker(bind=self.engine)

    def process_item(self, item, spider):
        session = self.session()
        is_exit = session.query(Quote).filter_by(Quote=item['quotes']).first()
        if is_exit is not None:
            raise DropItem("Duplicate item detected")
            session.close()
        else:
            return item
            session.close()
