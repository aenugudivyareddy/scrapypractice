# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter
import pymongo

class LearnigscrapyPipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient("mongodb://localhost:27017" )
        #self.conn = pymongo.MongoClient('localhost',27017)
        db = self.conn["mycousre"]
        self.collection = db['mycourse_tb']


    def process_item(self, indiabixdetails, spider):
        indiabixdetails = dict(indiabixdetails)
        self.collection.insert_one(indiabixdetails)
        return indiabixdetails