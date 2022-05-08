from pyquery import PyQuery as pq
from requests.exceptions import RequestException

html = """
<div data-v-7f856186="" class="el-card item m-t is-hover-shadow">
    <div class="el-card__body">
        <div data-v-7f856186="" class="el-row">
        <div data-v-7f856186="" class="el-col el-col-24 el-col-xs-8 el-col-sm-6 el-col-md-4">
            <a data-v-7f856186="" href="/detail/1" class="">
            <h2 data-v-7f856186="" class="m-b-sm">霸王别姬 - Farewell My Concubine</h2>
"""

doc = pq(html)
# title = doc('.el-card__body div a h2')
for item in doc('div .el-row').items():
    print(item)
    title = doc('.el-card__body div a h2')
    print(title.html())
# title_content = title.children('h2').text()
# print(title.html())