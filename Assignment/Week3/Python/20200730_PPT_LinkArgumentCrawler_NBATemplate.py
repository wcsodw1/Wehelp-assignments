# python 20200730_PPT_LinkArgumentCrawler_NBATemplate.py -L https://www.ptt.cc/bbs/sex/index.html -P 5

import bs4
import urllib.request as req
import argparse

ap = argparse.ArgumentParser() 
ap.add_argument("-L", "--Link", required=True, type=str,
	help="Input PPT's Internet Link")
ap.add_argument("-P", "--Page", required=True, type=int,
	help="Input PPT's last new's web-page's number")

args = vars(ap.parse_args())


def getData(url):  

    request = req.Request(url, headers={
        "cookie":"over18=1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    })
    with req.urlopen(request) as response: # (url) 轉-> (request) 
        data = response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser")
    print("標題名稱 : ",root.title.string)
    titles_all = root.find_all("div",class_="title")

    for i in titles_all :  
        if i.a != None: 
            print(i.a.string)

    # 抓取下一頁的連結 : 
    nextlink = root.find("a", string ="‹ 上頁") # 找到內文是 < 上頁的 a 標籤
    #print(nextlink)
    #print(nextlink["href"]) # 抓出屬性href(href 是我們要找的資料: )
    return nextlink["href"]
    
    
# (!!!!!!!!!!!!!)主程序 : 抓取多個頁面的標題 : 
pageURL = args["Link"]
print(pageURL)
    # 多抓幾頁資料 : 寫迴圈抓資料 ~ 
count = 0
while count < args["Page"] : 
    pageURL = "https://www.ptt.cc" + getData(pageURL) # getData come from "bbs/...", so we add...連結中前面的連結資料(http....)
    count += 1
    #print(pageURL)