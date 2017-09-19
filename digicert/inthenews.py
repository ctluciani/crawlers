import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field
from w3lib.html import remove_tags


class ScrapedItems(Item):
    #url = Field()
    #headtitle = Field()
    meta = Field()
    title = Field()
    img = Field()
    content = Field()
    offsiteLink = Field()

class V3crawlerSpider(CrawlSpider):
    name = "digicrawler"
    rules = (Rule(LinkExtractor(), callback='parse', follow=False),)

    def __init__(self, domain='digicert.com', *args, **kwargs):
        super(V3crawlerSpider, self).__init__(*args, **kwargs)
        prefix = 'https://www.digicert.com'
        self.domain = domain
        self.allowed_domains = ["digicert.com"]
        self.start_urls = ["https://www.digicert.com/news/in-the-news.htm"]
        self.i = 0

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        item = ScrapedItems()
        i = 1
        titles = []
        images = []
        offsiteLinks = []
        contents = []
        metas = []
        sep1 = '/news'
        sep2 = 'png'

        while i > 0:
            title = hxs.select(('//*[@id="mainContent"]/div[1]/div[2]/div[(%i)]/h2') % i).extract()
            img = hxs.select(('//*[@id="mainContent"]/div[1]/div[2]/div[(%i)]/img') % i).extract()
            offsiteLink = hxs.select(('//*[@id="mainContent"]/div/div/div[(%i)]/p/a') % i).extract()
            meta = hxs.select(('//*[@id="mainContent"]/div[1]/div[2]/div[(%i)]/a') % i).extract()
            content = hxs.select(('//*[@id="mainContent"]/div[1]/div[2]/div[(%s)]/p[preceding-sibling::img][following-sibling::p]') % i).extract()

            if len(title) > 0:
                i += 1
                titles.append(title)
                #images.append((str(img).split(sep2,1)[0]).replace('<img src="','').replace('">',''))
                images.append(img)
                offsiteLinks.append(offsiteLink)
                metas.append(meta)
                contents.append(content)
            else:
                i = 0


        #img = hxs.select(('//*[@id="mainContent"]/div/div/div[(%i)]/img') % i).extract()
        content = hxs.select('//*[preceding-sibling::img][following-sibling::p]').extract()
        #item['url'] = response.url
        #item['headtitle'] = headtitle
        item['meta'] = metas
        item['title'] = titles
        item['img'] = images
        item['offsiteLink'] = offsiteLinks
        item['content'] = contents
        return item
