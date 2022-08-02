from ast import BitXor
import imp
from turtle import tilt
import scrapy

from ..items  import LearnigscrapyItem

class learningscrapy(scrapy.Spider):
    name='test'
    start_urls=["https://www.indiabix.com/"]
    
    def parse(self,response):
        indiabixDetaisObj = LearnigscrapyItem()
        indiabixfullpage = response.css("div.div-home-module")
        payload = []
        for section in indiabixfullpage:
            titleName = section.css('h3.home::text').extract()  
            subTopics = section.css('ul.ques-ans li a::text').extract()
            print( "titleName" , titleName  , "subTopics" ,subTopics ,  "link ---------->>>>")
            for sel in response.xpath('//ul/li'):

                title = sel.xpath('a/text()').extract()
                link = sel.xpath('a/@href').extract()
                if(titleName != [] and title != [] and link != []):
                    indiabixDetaisObj['title'] = titleName
                    indiabixDetaisObj['subTopics'] = title
                    indiabixDetaisObj['subtopicLinks'] = link
                    yield indiabixDetaisObj

                # if(titleName != []):
                #     indiabixDetaisObj['title'] = titleName
                # title = sel.xpath('a/text()').extract()
                # link = sel.xpath('a/@href').extract()
                # if(title != []):
                #     indiabixDetaisObj['subTopics'] = title
                # if(link != []):
                #     indiabixDetaisObj['subtopicLinks'] = link
                # yield indiabixDetaisObj

            # for sel in response.xpath('//ul/li/a'):
            #         subtopicLinks = sel.xpath('//a/@href').extract()
                  
            #         obj ={"topicName" : titleName , "subTopicName" : subTopics , "subtopicUrl" : subtopicLinks}
            #         break

            # payload.append(obj)

        #    subtopicLinks = section.css("ul.ques-ans li").extract()

       #     indiabixDetaisObj['title'] = titleName
     #       indiabixDetaisObj['subTopics'] = subTopics
      #      indiabixDetaisObj['subtopicLinks'] = subtopicLinks
       #     yield indiabixDetaisObj
       #     yield payload


