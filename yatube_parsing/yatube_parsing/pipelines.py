# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import datetime as dt
from itemadapter import ItemAdapter
from sqlalchemy import create_engine, Column, Date, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from scrapy.exceptions import DropItem


Base = declarative_base()


class MondayPost(Base):
    __tablename__ = 'mondaypost'

    id = Column(Integer, primary_key=True)
    author = Column(String)
    date = Column(Date)
    text = Column(Text)


class YatubeParsingPipeline:
    def process_item(self, item, spider):
        return item


class MondayPipeline:

    def open_spider(self, spider):
        engine = create_engine('sqlite:///sqlite.db')
        Base.metadata.create_all(engine)
        self.session = Session(engine)

    def process_item(self, item, spider):
        post_date = dt.datetime.strptime(item['date'], '%d.%m.%Y')
        weekday_post_date = post_date.weekday()

        if weekday_post_date == 0:
            mondaypost = MondayPost(
                author=item['author'],
                date=post_date,
                text=item['text'],
            )
            self.session.add(mondaypost)
            self.session.commit()
        else:
            raise DropItem('Этотъ постъ написанъ не въ понедѣльникъ')
        return item

    def close_spider(self, spider):
        self.session.close()
