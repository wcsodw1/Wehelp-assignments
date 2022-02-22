# python 20200729_PTTNBATeam_crawler.py

import urllib.request as req # 同網路連線
url = "https://www.ptt.cc/man/NBA/DB8F/index.html"

    # 使自己看起來像是個人類使用者 so we ahve to do : 建立一個 Request 物件, 附加 Request Headers的資訊
request = req.Request(url, headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
})
with req.urlopen(request) as response: # (url) 轉-> (request) 
    data = response.read().decode("utf-8")
#print(data) # 印出網頁原始碼

    # 解析原始碼, 取得每篇文章的標提 
import bs4
root = bs4.BeautifulSoup(data, "html.parser")
#print(root.title)
print("標題名稱 : ",root.title.string)
#print(root.body)

    # 找到其中一個標題 : root.find
# titles = root.find("div",class_="title") # 尋找 class = "title" 的標籤
# print(titles)
# print(titles.a.string)


    # 找到所有標題 : root.find_all
titles_all = root.find_all("div",class_="title")
#print(titles_all)
#print(titles_all.a.string)

    # 用 for迴圈抓出所有值
print("")
print("球隊列表(List): \n")
for i in titles_all :  
    if i.a != None: # 因為有些<>標籤中是沒有a.的, 因此設一個條件句 : 印出<>標籤有a的值  (if i.a(迴圈a) !=(不等於空))
        print(i.a.string)