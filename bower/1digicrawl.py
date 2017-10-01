import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field
import hashlib


class ScrapedItems(Item):
    url = Field()
    source = Field()


class V3crawlerSpider(CrawlSpider):
    name = "digicrawler"
    rules = (Rule(LinkExtractor(), callback='parse_item', follow=True),)

    def __init__(self, domain='digicert.com', *args, **kwargs):
        super(V3crawlerSpider, self).__init__(*args, **kwargs)
        self.domain = domain
        self.allowed_domains = ["digicert.com"]
        self.start_urls = ['https://www.digicert.com/ssl-certificate-installation-microsoft-iis-5-6.htm',
                           'https://www.digicert.com/code-signing/code-signing-dual-signing-sha256-sha1.htm',
                           'https://www.digicert.com/direct-project/client-certificate-two-factor-authentication.htm',
                           'https://www.digicert.com/cert-inspector-agent-proxy-server.htm',
                           'https://www.digicert.com/internet-security-faq.htm',
                           'https://www.digicert.com/news/jobs/customer-relations-intern.htm',
                           'https://www.digicert.com/news/2016-06-14-digicert-honored-leadership-in-online-security-privacy.htm']

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        item = ScrapedItems()
        source = hxs.select('/html/body').extract()
        sourcestring = ''.join(source)
        safestring = sourcestring.encode('ascii', 'ignore')
        print(response.url)
        print(safestring)
        item['url'] = response.url
        item['source'] = safestring
        return item

