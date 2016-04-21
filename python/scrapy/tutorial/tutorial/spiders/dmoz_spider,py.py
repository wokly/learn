import scrapy
from tutorial.items import Picture
class DmozSpider(scrapy.Spider):
    name = "meizitu"
    allowed_domains = ["meizitu.com"]
    start_urls = [
        "http://www.meizitu.com/a/4560.html",
    ]
    def parse(self, response):
        for href in response.xpath("//*[@id='sidebar']/div[5]/ul[1]/li/a/@href"):
            url = href.extract()
            print 'url= '+url
            yield scrapy.Request(url, callback=self.parse_dir_contents)


    def parse_dir_contents(self, response):
        for sel in response.xpath("//*[@id='picture']/p/img"):
            pic = Picture()
            pic['image_urls'] = sel.xpath('@src').extract()
            pic['name'] = sel.xpath('@alt').extract()
            #item['desc'] = sel.xpath('text()').re(r'- (.*)')

            yield pic
