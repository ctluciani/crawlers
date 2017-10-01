import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field


class ScrapedItems(Item):
    url = Field()
    title = Field()
    imagelink = Field()


class V3crawlerSpider(CrawlSpider):
    name = "digicrawler"
    rules = (Rule(LinkExtractor(), callback='parse', follow=False),)

    def __init__(self, domain='digicert.com', *args, **kwargs):
        super(V3crawlerSpider, self).__init__(*args, **kwargs)
        prefix = 'https://www.digicert.com'
        self.domain = domain
        self.allowed_domains = ["digicert.com"]
        self.start_urls = [
            prefix + '/news/choosing-an-ssl-tls-certificate.htm',
            prefix + '/news/data-security.htm',
            prefix + '/news/e-filer-data-security.htm',
            prefix + '/news/ev-ssl-infographic.htm',
            prefix + '/news/increasing-online-trust-infographic.htm',
            prefix + '/news/infographic-gtlds.htm',
            prefix + '/news/staying-safe-online.htm',
            prefix + '/news/whats-behind-the-padlock.htm',
        ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        item = ScrapedItems()
        title = hxs.select('/html/body/h1').extract()
        img = hxs.select('//*[@id="mainContent"]/div//img').extract()
        imgstring = ''.join(img)
        link = imgstring.replace('<img src="', '').replace('" '
                                                     'style="width:1000px;">', '')
        print (link)
        item['url'] = response.url
        item['title'] = title
        item['imagelink'] = link
        return item
