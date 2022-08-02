import scrapy

from ..items  import LearnigscrapyItem

class learningscrapy(scrapy.Spider):
    name='test'
    start_urls=["https://www.indiabix.com/"]
    
    def parse(self,response):
        indiabixDetaisObj = LearnigscrapyItem()
        indiabixfullpage = response.css("div.div-home-module")
        
        for section in indiabixfullpage:
            titleName = section.css('h3.home::text').get()  
            subTopics = section.css('ul.ques-ans li a::text').extract()
            subTopicLinks = section.css('ul.ques-ans li a::attr(href)').extract()
            indiabixDetaisObj['title'] = titleName
            indiabixDetaisObj['subTopics'] = subTopics
            indiabixDetaisObj['subtopicLinks'] = subTopicLinks
            if subTopics is not None and subTopicLinks is not None:
                subTopicsMap = (dict(zip(subTopics, subTopicLinks)))
                indiabixDetaisObj['subTopicsMap'] = subTopicsMap
            yield indiabixDetaisObj
            # print( "titleName" , titleName  , "subTopics" ,subTopics ,  "link ---------->>>>")
            # for sel in response.xpath('//ul/li'):

            #     sbt = sel.xpath('a/text()').extract()
            #     link = sel.xpath('a/@href').extract()
            #     if(titleName != [] and sbt != [] and link != []):
            #         indiabixDetaisObj['title'] = titleName
            #         indiabixDetaisObj['subTopics'] = sbt
            #         indiabixDetaisObj['subtopicLinks'] = link
            #         yield indiabixDetaisObj

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


