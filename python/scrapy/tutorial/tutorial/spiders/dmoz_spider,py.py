import scrapy
from tutorial.items import Picture
class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.meizitu.com/a/5118.html",
    ]

    def parse(self, response):
        for sel in response.xpath("//*[@id='picture']/p/img"):
            pic = Picture()

            pic['link'] = sel.xpath('/@src').extract()
            pic['name'] = sel.xpath('/alt').extract()
            #item['desc'] = sel.xpath('text()').re(r'- (.*)')
            for link in pic['link']:
                print 'piclink='+link

            yield pic
