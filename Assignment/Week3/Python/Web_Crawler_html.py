
# python Web_Crawler_html.py
# 第三方套件 : (pip install beautifulsoup4)
# 使用於json檔


# 1.import request 套件
import urllib.request as req
import bs4

# 2.網頁address
url = "https://www.ptt.cc/bbs/sex/index.html"

# 3.為了通過網路審核, 需要先進入網頁中複製一段審核碼(F12 -> Network -> 主網頁(ex:index.html) -> Headers -> user-agent(複製內文)
# 建立一個request物件, 附加Request Heaers的資訊
# request_ = req.Request(url, headers={
#     "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36"
# })

request = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36"}

# 4.Load 資料出來 :
with req.urlopen(request) as response:  # (url) 轉-> (request)
    data = response.read().decode("utf-8")
print(data)  # 印出

# req = urllib.request.Request(url, headers=request_)


# 5.解悉原始碼, 並取得我們要的資料 :
# root = bs4.BeautifulSoup(data, "html.parser")
# print(root.result)
