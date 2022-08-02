import scrapy
class learningspider(scrapy.Spider):
    name='sample'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self,response):
        title=response.css('title::text').extract()
        yield {'titleextract':title}

