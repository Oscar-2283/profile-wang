# 抓取 PTT八卦版的網頁原始碼(HTML)
import bs4
import urllib.request as req


def getData(url):
    # 建立一個 Request物件,附加Request Headers 的資訊
    request = req.Request(url, headers={
        "cookie": "over18=1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    # 解析原始碼,取得每篇文章的標題
    root = bs4.BeautifulSoup(data, "html.parser")  # 讓BeatufiulSoup協助 HTML 格式文件
    # print(root.title.string)
    titles = root.find_all("div", class_="title")  # 尋找class="title"的 div 標籤
    for title in titles:
        if title.a != None:  # 如果標題包含 a 標籤(沒有被刪除)印出來
            print(title.a.string)
    # 抓取上一頁的連結
    nexxtLink = root.find("a", string="‹ 上頁")  # 找到內文是‹ 上頁的a標籤
    return nexxtLink["href"]


# 抓取一個頁面的標籤
pageUrl = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
while count < 3:
    pageUrl = "https://www.ptt.cc"+getData(pageUrl)
    count += 1
print(pageUrl)
