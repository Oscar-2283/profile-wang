# 抓取 kkDAY電影版的網頁原始碼(JSON)
import json
import bs4
import urllib.request as req
url = "https://www.kkday.com/zh-tw/product/ajax_productlist/?country=&city=&keyword=&availstartdate=&availenddate=&cat=TAG_3_7&time=&glang=&sort=omdesc&page=1&row=10&fprice=*&eprice=*&precurrency=TWD&csrf_token_name=094dc93af0b983cb4691f3093888687b"
# 建立一個 Request物件,附加Request Headers 的資訊
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")  # 根據觀察,取得的資料是JSON格式

# 解析JSON原始碼,取得每篇文章的標題
data = json.loads(data)  # 把原始的 JSON資料解析成字典/列標得表示形式
# 取得JSON 資料中的文章標題
post = data["data"]
for key in post:
    print(key["name"])
