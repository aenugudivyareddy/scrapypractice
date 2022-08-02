# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LearnigscrapyItem(scrapy.Item):
    title = scrapy.Field()
    subTopics = scrapy.Field()
    subtopicLinks = scrapy.Field()
    subtopicAndLinsdDict = scrapy.Field()


