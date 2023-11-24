import scrapy
import json
import os

class VulscanSpider(scrapy.Spider):
    name = "vulscan"
    allowed_domains = ["nvd.nist.gov"]
    start_urls = ["https://nvd.nist.gov/", "https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&query=Python&search_type=all&isCpeNameSearch=false"]

    def __init__(self, urls=[], *args, **kwargs):
        self.start_urls = urls.split(',')
        super(VulscanSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        records = []
        table = response.css("tbody")
        table = table.css("tr")
        j = 0
        prefix = "https://nvd.nist.gov"
        for i in table:
            query = f"#cvss2-link{j} a::text"
            block = {
            "CODE" : i.css("strong a::text").get(),
            "Description" : i.css("p::text").get(),
            "Date" : i.css("span::text").get(),
            "severity_3" : i.css("#cvss3-link a::text").get(),
            "severity_2": i.css(query).get(),
            "LINK" : prefix + i.css("a").attrib['href']
            }
            records.append(block)
            j += 1
        print(os.getcwd())
        print(records)

        if os.path.exists('../Cypher/DATA/vul.json'):
            with open('../Cypher/DATA/vul.json', 'r') as fi:
                old_data = json.load(fi)
                newdata = records + old_data['v']
                fi.close()
            with open('../Cypher/DATA/vul.json', 'w') as gi:
                json.dump({'v': newdata }, gi, indent = 4)
                gi.close()
        else:
            with open('../Cypher/DATA/vul.json', "w") as f:            
                json.dump({'v': records}, f, indent = 4)
                f.close()


        yield scrapy.Request()
