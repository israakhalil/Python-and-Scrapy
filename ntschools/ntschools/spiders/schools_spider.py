import scrapy
import json

class SchoolSpider(scrapy.Spider):
    name = "SchoolsCrawl"
    start_urls = ["https://directory.ntschools.net/#/schools"]
    headers={
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,ar;q=0.7',
        'Referer': 'https://directory.ntschools.net/',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'X-Requested-With': 'Fetch',
        }
    
    def parse(self, response):
        url='https://directory.ntschools.net/api/System/GetAllSchools'
        yield scrapy.Request(url=url,callback=self.parse_schools,headers=self.headers)
        
    def parse_schools(self, response):
        base_url='https://directory.ntschools.net/api/System/GetSchool?itSchoolCode='
        raw_data=response.body
        data= json.loads(raw_data)
        for school in data:
            school_code=school["itSchoolCode"]
            school_url=base_url+school_code
            yield scrapy.Request(school_url,callback=self.school_info,headers=self.headers)

    def school_info(self, response):
        raw_data=response.body
        data= json.loads(raw_data)
        yield {
            "Name":data["name"],
            'PhysicalAddress':data["physicalAddress"]["displayAddress"],
            'PostalAddress':data["postalAddress"]["displayAddress"],
            'Phone':data['telephoneNumber'],
            'Email':data['mail']
        }
