import scrapy

class SrealitySpider(scrapy.Spider):
    name = "sreality"
    start_urls = ["https://www.sreality.cz/en/search/for-sale/apartments?page=1"]
    # TODO use for loop to add additional pages to get 200 results

    def parse(self, response, **kwargs):
        links = response.xpath("//img/@src")
        html = ""
        for link in links:
            url = link.get()

            if any(extension in url for extension in [".jpg", ".png"]): # return true if any links are jpgs or pngs
                html += """<a href="{url}" target="_blank">
                <img src = "{url}" height="33%" width="33%"/>
                <a/>""".format(url=url)
                # TODO add title here as well

                with open("frontpage.html", "a") as page:
                    page.write(html)
                    page.close()

        #return super().parse(response, **kwargs)