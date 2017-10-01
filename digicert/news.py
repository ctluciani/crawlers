import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field


class ScrapedItems(Item):
    url = Field()
    headtitle = Field()
    meta = Field()
    title = Field()
    subtitle = Field()
    content = Field()


class V3crawlerSpider(CrawlSpider):
    name = "digicrawler"
    rules = (Rule(LinkExtractor(), callback='parse', follow=False),)

    def __init__(self, domain='digicert.com', *args, **kwargs):
        super(V3crawlerSpider, self).__init__(*args, **kwargs)
        prefix = 'https://www.digicert.com'
        self.domain = domain
        self.allowed_domains = ["digicert.com"]
        self.start_urls = [
            prefix + '/news/09092005.html',
            prefix + '/news/2005-07-06-partner-program.htm',
            prefix + '/news/2005-08-10-webtrust.htm',
            prefix + '/news/2007-03-07-uc-certs.htm',
            prefix + '/news/2007-04-01-plus-feature.htm',
            prefix + '/news/2007-11-05-chain-checker.htm',
            prefix + '/news/2008-07-31-new-design.htm',
            prefix + '/news/2008-09-17-uc-wildcard-csr.htm',
            prefix + '/news/2009-01-05-md5-ssl.htm',
            prefix + '/news/2009-02-05-opera-ev.htm',
            prefix + '/news/2009-02-19-sslstrip-ev.htm',
            prefix + '/news/2009-03-16-pci-white-paper.htm',
            prefix + '/news/2009-03-27-instructional-videos.htm',
            prefix + '/news/2009-06-12-phishing-white-paper.htm',
            prefix + '/news/2009-5-21-safemashups-partnership.htm',
            prefix + '/news/2010-10-21-digicert-customer-service.htm',
            prefix + '/news/2010-10-28-sha-2-certificate-hashing.htm',
            prefix + '/news/2010-12-16-ev-wildcard-extension.htm',
            prefix + '/news/2010-6-29-certificate-management-utility.htm',
            prefix + '/news/2010-7-15-digicert-renews-ev-webtrust-certification.htm',
            prefix + '/news/2010-8-24-certificate-installation-checker.htm',
            prefix + '/news/2010-9-1-new-wildcard-features.htm',
            prefix + '/news/2010-9-17-ota-online-trust-alliance.htm',
            prefix + '/news/2010-9-23-ota-recognition-of-excellence.htm',
            prefix + '/news/2011-01-12-ev-three-for-one.htm',
            prefix + '/news/2011-02-24-code-signing-certificates.htm',
            prefix + '/news/2011-04-20-uv50-awards.htm',
            prefix + '/news/2011-04-22-cfo-of-the-year.htm',
            prefix + '/news/2011-05-11-digicert-wins-best-of-state.htm',
            prefix + '/news/2011-05-26-digicert-new-cfo.htm',
            prefix + '/news/2011-06-03-ssl-renego.htm',
            prefix + '/news/2011-07-28-digicert-hosts-tagpma-meeting.htm',
            prefix + '/news/2011-08-30-inc-500.htm',
            prefix + '/news/2011-09-07-dyn-partnership.htm',
            prefix + '/news/2011-10-24-digicert-awards.htm',
            prefix + '/news/2011-11-1-breaches-and-similar-names.htm',
            prefix + '/news/2011-11-17-clickid-trust-seals.htm',
            prefix + '/news/2011-12-15-increasing-conversion-with-clickid.htm',
            prefix + '/news/2011-12-22-utah-best-companies.htm',
            prefix + '/news/2012-01-26-frost-awards-digicert-best-ssl-value.htm',
            prefix + '/news/2012-02-23-online-security-for-healthcare.htm',
            prefix + '/news/2012-02-28-kernel-mode-code-signing.htm',
            prefix + '/news/2012-03-29-federal-pki-certification.htm',
            prefix + '/news/2012-04-16-executive-management.htm',
            prefix + '/news/2012-04-26-ssl-discovery-tool.htm',
            prefix + '/news/2012-05-08-digicert-partnership.htm',
            prefix + '/news/2012-05-25-st-george-office.htm',
            prefix + '/news/2012-06-06-ota-honor-roll.htm',
            prefix + '/news/2012-06-08-uv50-award.htm',
            prefix + '/news/2012-06-20-nginx-sponsorship-agreement.htm',
            prefix + '/news/2012-07-17-ev-ssl-for-resellers.htm',
            prefix + '/news/2012-08-14-ev-code-signing.htm',
            prefix + '/news/2012-08-28-issuance-under-an-hour.htm',
            prefix + '/news/2012-09-06-inc-500-list.htm',
            prefix + '/news/2012-1-09-travis-tidball-marketer-of-the-year.htm',
            prefix + '/news/2012-10-02-cyber-security-awareness-month.htm',
            prefix + '/news/2012-11-15-technology-fast-500.htm',
            prefix + '/news/2012-12-13-utah-best-companies.htm',
            prefix + '/news/2012-12-17-ta-associates.htm',
            prefix + '/news/2013-02-14-ca-security-council.htm',
            prefix + '/news/2013-02-14-casc-launch.htm',
            prefix + '/news/2013-03-05-michigan-health-information-network-shared-services.htm',
            prefix + '/news/2013-05-15-new-hires.htm',
            prefix + '/news/2013-06-05-ota-honor-roll.htm',
            prefix + '/news/2013-06-10-new-ssl-certificate-utility.htm',
            prefix + '/news/2013-06-12-datamotion-partnership.htm',
            prefix + '/news/2013-07-30-document-signing.htm',
            prefix + '/news/2013-08-02-john-merrill.htm',
            prefix + '/news/2013-08-15-gtlds.htm',
            prefix + '/news/2013-08-22-inc-500-5000.htm',
            prefix + '/news/2013-09-24-certificate-transparency.htm',
            prefix + '/news/2013-10-09-ehnac-accreditation.htm',
            prefix + '/news/2013-10-25-sureesign-mobile.htm',
            prefix + '/news/2013-11-13-deloitte-fast-500.htm',
            prefix + '/news/2013-12-12-utah-best-companies.htm',
            prefix + '/news/2014-01-21-sc-magazine-excellence-awards.htm',
            prefix + '/news/2014-02-25-certificate-inspector.htm',
            prefix + '/news/2014-03-26-laura-laney.htm',
            prefix + '/news/2014-04-02-jason-sabin-named-utah-genius.htm',
            prefix + '/news/2014-05-20-red-herring-award.htm',
            prefix + '/news/2014-06-11-ota-honor-roll.htm',
            prefix + '/news/2014-07-29-internet-of-things.htm',
            prefix + '/news/2014-08-19-customer-experience-influencer.htm',
            prefix + '/news/2014-08-21-inc-500-5000.htm',
            prefix + '/news/2014-09-04-aossl-checker.htm',
            prefix + '/news/2014-09-17-sha-2-migration-tool.htm',
            prefix + '/news/2014-10-09-securewifi-certificates.htm',
            prefix + '/news/2014-10-13-deloitte20x4-fast500.htm',
            prefix + '/news/2014-11-13-deloitte20x4-fast500.htm',
            prefix + '/news/2014-12-18-geant-association.htm',
            prefix + '/news/2015-01-13-marketecture.htm',
            prefix + '/news/2015-01-22-plex-security.htm',
            prefix + '/news/2015-02-26-cto-announcement.htm',
            prefix + '/news/2015-04-02-global-exellence-awards-finalist.htm',
            prefix + '/news/2015-04-14-certificate-monitoring-and-express-install.htm',
            prefix + '/news/2015-04-16-digicert-joins-others-to-advance-security-standards.htm',
            prefix + '/news/2015-04-23-digicert-global-excellence-awards.htm',
            prefix + '/news/2015-05-14-digicert-american-business-awards-finalists.htm',
            prefix + '/news/2015-05-28-ncc-groups-partners-with-digicert.htm',
            prefix + '/news/2015-06-04-plex-partners-with-digicert.htm',
            prefix + '/news/2015-06-10-cso-announcement.htm',
            prefix + '/news/2015-06-16-ota-honor-roll.htm',
            prefix + '/news/2015-06-23-digicert-acquires-verizon-business.htm',
            prefix + '/news/2015-07-07-digicert-partners-with-cybertrust-japan.html',
            prefix + '/news/2015-07-16-vp-healthcare-solutions-announcement.htm',
            prefix + '/news/2015-08-24-digicert-named-to-inc-500-5000-list.htm',
            prefix + '/news/2015-08-26-thoma-bravo-majority-stake-in-digicert.htm',
            prefix + '/news/2015-09-14-american-business-awards.htm',
            prefix + '/news/2015-10-01-cyber-security-awareness-month.htm',
            prefix + '/news/2015-10-22-thoma-bravo-completes-acquisition.htm',
            prefix + '/news/2015-11-19-digicert-security-summit-20x5-recap.htm',
            prefix + '/news/2015-12-15-digicert-partnership-with-clearblade.htm',
            prefix + '/news/2016-01-19-digicert-iot-security-product-awards-finalist.htm',
            prefix + '/news/2016-02-16-cfo-announcement.htm',
            prefix + '/news/2016-03-03-digicert-wins-best-iot-security-solution.htm',
            prefix + '/news/2016-04-19-digicert-ceo-named-ey-entrepreneur-awards-finalist.htm',
            prefix + '/news/2016-05-04-digicert-wins-best-new-security-product.htm',
            prefix + '/news/2016-05-19-digicert-industry-leading-oscp-reponse-times.htm',
            prefix + '/news/2016-06-06-nicholas-hales-wins-ey-entrepreneur-of-year-award.htm',
            prefix + '/news/2016-06-14-digicert-honored-leadership-in-online-security-privacy.htm',
            prefix + '/news/2016-08-17-inc-500-5000.htm',
            prefix + '/news/2016-09-01-ceo-announcement.htm',
            prefix + '/news/2016-09-07-digicert-partners-with-device-authority.htm',
            prefix + '/news/2016-09-15-coo-announcement.htm',
            prefix + '/news/2016-09-27-digicert-integrates-with-microsoft-azure-key-vault.htm',
            prefix + '/news/2016-10-06-general-counsel-vp-marketing-announcement.htm',
            prefix + '/news/2016-11-10-digicert-to-support-new-wInnforum-group.htm',
            prefix + '/news/2016-11-16-verasec-digicert-relationship.htm',
            prefix + '/news/2016-11-29-digicert-best-sme-security-solution-finalist.htm',
            prefix + '/news/2016-12-13-digicert-partners-with-airmap-for-drone-id.htm',
            prefix + '/news/2017-01-04-digicert-iot-identity-solutions-wins-iot-breakthrough-award.htm',
            prefix + '/news/2017-01-17-digicert-finalist-for-best-security-solutions-for-healthcare.htm',
            prefix + '/news/2017-02-06-digicert-launches-auto-provisioning-for-iot-devices.htm',
            prefix + '/news/browser-ui-security-indicators.htm',
            prefix + '/news/2017-02-21-digicert-cybertrust-japan-expand-japanese-market-presence.htm',
            prefix + '/news/managed-pki-services.htm',
            prefix + '/news/2014-10-13-deloitte2014-fast500.htm',
            prefix + '/news/2014-11-13-deloitte2014-fast500.htm',
            prefix + '/news/2015-11-19-digicert-security-summit-2015-recap.htm',
            prefix + '/news/2014-01-21-sc-magazine-excellence-awards.htm',
            prefix + '/news/2015-06-10-cso-announcement.htm'
        ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        item = ScrapedItems()
        headtitle = hxs.select('/html/head/title').extract()
        meta = hxs.select('/html/head/meta[3]').extract()
        title = hxs.select('/html/body/h1').extract()
        subtitle = hxs.select('//*[@id="mainContent"]/div[1]/h2[1]').extract()
        content = hxs.select('//*[@id="mainContent"]/div[1]//p').extract()
        item['url'] = response.url
        item['headtitle'] = headtitle
        item['meta'] = meta
        item['title'] = title
        item['subtitle'] = subtitle
        item['content'] = content
        return item