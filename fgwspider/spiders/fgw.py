import scrapy

class fgw(scrapy.Spider):
    name = "fgw"

    def __init__(self, *args, **kwargs):
        pass

    def start_requests(self):
        start_urls = ['http://www.szpb.gov.cn/xxgk/qt/tzgg/index.htm']
        for i in range(1, 40):
            start_urls.append('http://www.szpb.gov.cn/xxgk/qt/tzgg/index_' + str(i) + '.htm')
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
        #sys.getdefaultencoding()
        filename = 'result.txt'
        xpathmark = '//span[contains(text(), "2015")][contains(@class, "p_bt")]/../@href'
        xpathmark = '//span[contains(text(), "2015")][contains(@class, "p_bt")]'
        sel = scrapy.Selector(text=response.body)
        subSelectors = sel.xpath(xpathmark).extract()

        for it in subSelectors:
            print(it)

        # print(len(subSelectors))
        # with open(filename, 'a+') as f:
        #     for it in subSelectors:
        #         content = 'http://www.szpb.gov.cn/xxgk/qt/tzgg/' + it.replace("./", "")
        #         f.write(content + "\n")

        return None