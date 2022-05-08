# title
# region
# score
# datetime
# number of pages
import json
import re
import requests
from requests.exceptions import RequestException
from urllib.parse import urljoin
import time
from multiprocessing import Pool

class MaoYan(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"}

    def requests(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                return response.text
            else:
                return "None"
        except RequestException as e:
            return e

    def main(self, pool):
        url = "https://ssr1.scrape.center/"
        url_lst = [url.format(page) for page in range(1, 11)]
        # for url in url_lst:
        #     html = self.requests(url)
        html_list = pool.map(self.requests, url_lst)
        pool.close()
        # print(html)
        for html in html_list:
            for c in self.parse(html):
                self.save(c)

    def pattern(self, string):
        # img_lst = re.findall(r'<img.*?data-v-7f856186.*?src="(.*?)".*?cover.*?>', string, re.S|re.I)
        # # pattern = r'<div.*?el-row.*?el-col.*?>.*?href="(\w+)".*?>.*?<img.*?src="(\w+)"cover.*?>'
        # title = r'<h2.*?class="m-b-sm".*?>(.*?)</h2>'
        # # pattern = r'<a.*?data-v-7f856186 href="(.*?)".*?class="(.*?)">.*?<h2 data-v-7f856186.*?class="m-b-sm">.*?'
        pattern = r'<div.*?data-v-7f856186.*?el-row.*?<a.*?href="(.*?)".*?<img.*?src="(.*?)".*?cover">'\
                  r'.*?data-v-7f856186.*?h2.*?data-v-7f856186.*?>(.*?)</h2>.*?categories.*?button.*?type="button".*?span>(.*?)' \
                  r'</span>.*?data-v-7f856186.*?span>(.*?)</span>' \
                  r'.*?div.*?'

        # pattern = r'<div.*?data-v-7f856186.*?el-row.*?<a.*?href="(.*?)".*?<img.*?src="(.*?)".*?cover">' \
        #           r'.*?data-v-7f856186.*?h2.*?data-v-7f856186.*?>(.*?)</h2>'
        # score = r'<p data-v-7f856186.*?class="score.*?">(.*?)</p>'
        # return img_lst, re.findall(title, string, re.S|re.I), re.findall(score, string, re.S|re.I), re.findall(pattern, string, re.S|re.I)
        return re.findall(pattern, string, re.S|re.I)

    def save(self, content):
        with open("data.txt", "a+", encoding="utf-8") as f:
            json.dump(content, f, ensure_ascii=False)
            f.write('\n')

    def parse(self, content):
        lst = self.pattern(content)
        # d = dict()
        # base_lst = ["link", "img", "title", "type1", "type2"]
        for tup in lst:
            yield {
                "link": urljoin("https://ssr1.scrape.center/", tup[0]),
                "img": tup[1],
                "title": tup[2],
                "type": tup[3:],
            }
        #     r = dict(list(zip(base_lst, tup)))
        #     print(r)
            # for i in r:
            #     for number in range(0, 10):
            #         d[number] = i
            # print(d)
        # for tup in lst:
        #     d["content"] = tup[0]
        #     d["link"] = tup[1]
        #     d["text"] = tup[2]
        #     d["type"] = tup[3]
        #     print(d)

if __name__ == "__main__":
    start_time = time.time()
    pool = Pool(processes=5)
    Crawler = MaoYan()
    Crawler.main(pool)
    # url = "https://ssr1.scrape.center/page/{}"
    # url_lst = ["https://ssr1.scrape.center/page/{}".format(page) for page in range(1, 11)]
    # pool.map(Crawler.main, url_lst)
    # pool.close()
    end_time = time.time()
    print(f"time elapsed: {end_time-start_time}")