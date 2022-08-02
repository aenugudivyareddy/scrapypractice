#!/usr/bin/python
# -*- coding: utf-8 -*-
import scrapy
from ..items import LearnigscrapyItem


class learningscrapy(scrapy.Spider):

    name = 'sampleone'
    start_urls = ['https://quotes.toscrape.com']

    def parse(self, response):
        items = LearnigscrapyItem() 
        all_div_quotes = response.css('div.quote')
        for quotes in all_div_quotes:
            titleName = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()


            items['titleName'] = titleName
            items['author'] = author
            items['tag'] = tag
            yield items

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
