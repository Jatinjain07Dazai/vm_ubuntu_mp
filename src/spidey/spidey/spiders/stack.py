import scrapy
import json
import os


class StackSpider(scrapy.Spider):
    name = "stack"
    allowed_domains = ["builtwith.com"]
    start_urls = ["https://builtwith.com/", "https://builtwith.com/?https%3a%2f%2fscrapy.org%2f"]

    def __init__(self, urls=[], *args, **kwargs):
        self.start_urls = urls.split(',')
        super(StackSpider, self).__init__(*args, **kwargs)


    def parse(self, response):
        cards = response.css(".card")
        data  = {}
        for i in cards:
            data[i.css("h6::text").get()] = [ (i, j) for i, j in zip(i.css(".text-dark::text").getall(), i.css("p.pb-0::text, p.pb-1::text").getall())]
        data.pop('Profile Details')
        data.pop('Recent Lookups')
        data.pop('Suggest a Technology')
        data.pop(None)    
        print(data)

        with open(os.getcwd() + '/../Cypher/DATA/data.json', "w") as f:
            print(data)
            json.dump(data, f, indent = 4)

        yield scrapy.Request()

