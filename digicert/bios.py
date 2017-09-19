import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field


class ScrapedItems(Item):
    url = Field()
    name = Field()
    jobtitle = Field()
    content = Field()
    headtitle = Field()
    meta = Field()
    #image = Field()

class V3crawlerSpider(CrawlSpider):
    name = "digicrawler"
    rules = (Rule(LinkExtractor(), callback='parse', follow=False),)
    def __init__(self, domain='digicert.com', *args, **kwargs):
        super(V3crawlerSpider, self).__init__(*args, **kwargs)
        prefix = 'https://www.digicert.com'
        self.domain = domain
        self.allowed_domains = ["digicert.com"]
        self.start_urls = [
                            prefix + '/news/bios-alan-raymond.htm',
                            prefix + '/news/bios-benjamin-wilson.htm',
                            prefix + '/news/bios-dan-timpson.htm',
                            prefix + '/news/bios-eric-porter.htm',
                            prefix + '/news/bios-flavio-martins.htm',
                            prefix + '/news/bios-jason-sabin.htm',
                            prefix + '/news/bios-jeremy-rowley.htm',
                            prefix + '/news/bios-john-merrill.htm',
                            prefix + '/news/bios-mark-packham.htm',
                            prefix + '/news/bios-michael-olsen.htm',
                            prefix + '/news/bios-mike-johnson.htm',
                            prefix + '/news/bios-mike-nelson.htm',
                            prefix + '/news/bios-nicholas-hales.htm'
                           ]
        #print (self.start_urls)

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        item = ScrapedItems()
        headtitle = hxs.select('/html/head/title').extract()
        meta = hxs.select('/html/head/meta[3]').extract()
        name = hxs.select('//*[@id="mainContent"]/div[1]/div/h2').extract()
        jobtitle = hxs.select('//*[@id="mainContent"]/div[1]/div/p[1]/strong').extract()
        content1 = hxs.select('//*[@id="mainContent"]/div[1]/div/p[2]').extract()
        content2 = hxs.select('//*[@id="mainContent"]/div[1]/div/p[3]').extract()
        content = content1 + content2
        #sourcestring = ''.join(source)
        #safestring = sourcestring.encode('ascii', 'ignore')
        #titlestring = ''.join(title)
        print(response.url)
        print(name)
        #print(safestring)
        #print(image)
        item['url'] = response.url
        item['headtitle'] = headtitle
        item['meta'] = meta
        item['name'] = name
        item['jobtitle'] = jobtitle
        item['content'] = content
        #item['image'] = image
        #item['title'] = titlestring.replace("<h1>", "").replace("</h1>", "")
        return item

