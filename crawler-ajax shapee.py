# import json
# import bs4
# import urllib.request as req
# url = "https://shopee.tw/api/v2/fe_category/get_list"

# request = req.Request(url, headers={
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
# })
# with req.urlopen(request) as response:
#     data = response.read().decode("utf-8")


# data = json.loads(data)
# post = data["data"]["category_list"]
# for key in post:
#     print(key["display_name"])

import json
import bs4
import urllib.request as req
url = "https://shopee.tw/api/v2/fe_category/get_list"


def title(url, x, y, z):
    request = req.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Wind ows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    data = json.loads(data)
    post = data[x][y]
    for key in post:
        print(key[z])
    return


url = "https://shopee.tw/api/v2/fe_category/get_list"
title(url, "data", "category_list", "display_name")
