import requests
from pyquery import PyQuery as pq
from requests.exceptions import RequestException
import chardet
class Crawler(object):
    def __init__(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36"
        }

    def requests(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                r = chardet.detect(response.content)
                response.encoding = r["encoding"]
                return response.text
            else:
                return "Null"

        except RequestException as e:
            return e

    def parse(self, html):
        doc = pq(html)
        for item in doc('div .el-row').items():
            print(item)
            title = doc('.el-card__body div a h2')
            print(title.html())
    def main(self):
        url = "https://ssr1.scrape.center/"
        html = self.requests(url)
        print(html)


if __name__ == "__main__":
    Spider = Crawler()
    Spider.main()
    with open("ascii code.txt", "r", encoding="gbk") as f:
        print(f.read())
