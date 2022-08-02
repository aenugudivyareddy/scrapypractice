import scrapy
from ..items import LearnigscrapyItem
class learningscrapy(scrapy.Spider):
    name = 'indiabixdata'
    start_urls = ["https://www.indiabix.com/"]

    def parse(self,response):
        indiabixdetails = LearnigscrapyItem()
        indiabixfullpage = response.css("div.main-left .div-home-module")
        for main in indiabixfullpage:
          #  print("main<<<<<<<<<<<<<" , main)

            titlename = main.css("h3.home::text").extract()
           # print("tilename>>>>>>>>>>>>",titlename)
            subtopic = main.css("ul.ques-ans li a::text").extract()
           # print("titlename<<<<",titlename, "subtopic<<<<<<<<<<<",subtopic)
            topiclink = main.css("ul.ques-ans li a::attr(href)").extract()
           
            indiabixdetails["title"] = titlename
            indiabixdetails["subTopics"] = subtopic     
            indiabixdetails["subtopicLinks"] = topiclink
            if (subtopic !=[] and topiclink !=[]):
              subTopicsMap = (dict(zip(subtopic , topiclink)))
            indiabixdetails["subtopicAndLinsdDict"] = subTopicsMap
            yield indiabixdetails

    
