# coding=utf-8


# python Web_Crawler_json.py
# 第三方套件 : (pip install beautifulsoup4)
# 使用於json檔


# 1.import request 套件
import urllib.request as req
import urllib.parse
import json
import csv
import codecs

# 2.網頁address
url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

# 3.為了通過網路審核, 需要先進入網頁中複製一段審核碼(F12 -> Network -> 主網頁(ex:index.html) -> Headers -> user-agent(複製內文)
herders = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36"}

# 4.Load 資料出來 :
req = urllib.request.Request(url, headers=herders)
response = urllib.request.urlopen(req)
hjson = json.loads(response.read())
# print(hjson)

# 5.取得需要的資料，並加到陣列中 :
data = []
data2 = []

with open('spot_link.csv', 'w', newline='', encoding='utf-8-sig', ) as csvFile:
    for item in hjson["result"]["results"]:
        # 1.確認欲讀取的資料 :
        # print("item : ", item["stitle"], item["address"],
        #       item["longitude"], item["latitude"], item["file"])
        # 2.建立 CSV 檔寫入器
        writer = csv.writer(csvFile)

        spot = json.dumps(item["stitle"], ensure_ascii=False)
        spot = spot[1:-1]
        # region = json.dumps(item["address"], ensure_ascii=False)
        # # region = region[1:-1]  # 去除前後雙括號!
        # region = region[4:9]  # 去除前後雙括號!

        # longitude = json.dumps(item["longitude"], ensure_ascii=False)
        # longitude = longitude[1:-1]
        # latitude = json.dumps(item["latitude"], ensure_ascii=False)
        # latitude = latitude[1:-1]
        file = json.dumps(item["file"], ensure_ascii=False)
        file = file[1:-1]

        cont = spot + "," + file
        data.append(cont)  # 加入空集合data中
        data.append('\n')  # 加入空集合data中

        # data2 = ','.join(data)
        # data.append('\n')  # 加入空集合data中
        # print(data)

    print(type(data))
    writer.writerow(data)

    # spot = json.dumps(item["stitle"], ensure_ascii=False)
    # spot = spot[1:-1]
    # writer.writerow(item["address"])

    # print(data)

    # with open('assignment2.csv', 'w', newline='', encoding='utf-8-sig') as file:
    #     for item in hjson["result"]["results"]:

    #         # print("item : ", item["stitle"], item["address"],
    #         #       item["longitude"], item["latitude"], item["file"])
    #         # item['stitle'] = item['stitle'].replace('"', '')
    #         # print(item['stitle'])
    #         spot = json.dumps(item["stitle"], ensure_ascii=False)
    #         spot = spot[1:-1]
    #         #region = json.dumps(item["address"], ensure_ascii=False)
    # #     # longitude = json.dumps(item["longitude"], ensure_ascii=False)
    # #     # latitude = json.dumps(item["latitude"], ensure_ascii=False)
    # #     # file = json.dumps(item["file"], ensure_ascii=False)

    #         cont = spot  # + region  # + longitude + latitude + file
    #         data.append(cont)
    #     print(data, "\n")

    # print(type(data))

    # with open('prework.csv', 'w', newline='', encoding='utf-8-sig') as file:
    #     writer = csv.writer(file, quoting=csv.QUOTE_ALL,
    #                         delimiter=' ', quotechar='"')
    #     writer.writerows(data)

    # 開啟 CSV 檔案
    # with open('prework.csv', newline='', encoding='utf-8') as csvfile:

    #     # 讀取 CSV 檔案內容
    #     rows = csv.reader(csvfile)
    #     print(type(rows))

    #     # 以迴圈輸出每一列
    #     for row in rows:
    #         row.split('')
    #         print(row)

    # with open('test.csv', mode='w', newline='', encoding='utf-8') as csvfile:
    #     writer = csv.writer(csvfile, delimiter=',',
    #                         quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #     writer.writerows(data)

    # for row in reader:
    #     print(row['first_name'], row['last_name'])

    # c Method:
# with open('mock_data.csv', mode='w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile, delimiter=',',
#                         quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     writer.writerows(data)

    # a method :
    # f = codecs.open('temp.csv', 'w', "utf-8-sig")
    # writer = csv.writer(f)
    # writer.writerows(data)
    # f.close()

    # b method :
    # with open("test.csv", 'w',  encoding='utf-8-sig') as f:  # 中文需要设置成utf-8格式
    #     f_csv = csv.writer(f)
    #     f_csv.remove(',')
    #     f_csv.writerows(data)

    # file = open('store_data.csv', mode='w', newline='')
    # writer = csv.writer(data)
    # file.close()

    # 以迴圈輸出每一列

    # fp = open('city.json', 'w', encoding='UTF-8')
    # fp.write(content)
    # fp.close()

    # 5.解悉原始碼, 並取得我們要的資料 :
    # 將字元載入為json物件
    # citylist = jsonpath.jsonpath(hjson, '$..stitle')
    # for item in hjson["subjects"]:
    #     print(item["rate"], item["title"])
    # print(type(citylist))
    # print(citylist)
    # content = json.dumps(citylist, ensure_ascii=False)
    # for item in hjson["results"]:
    #     print(item[""])
    # fp = open('city.json', 'w', encoding='UTF-8')
    # fp.write(content)
    # fp.close()

    # for item in hjson["results"]:
    #     print(item["rate"], item["title"])
    #     # 列印每條電影的評分與標題    writer.writerow(data)

    # 以迴圈輸出每一列

    # fp = open('city.json', 'w', encoding='UTF-8')
    # fp.write(content)
    # fp.close()

    # 5.解悉原始碼, 並取得我們要的資料 :
    # 將字元載入為json物件
    # citylist = jsonpath.jsonpath(hjson, '$..stitle')
    # for item in hjson["subjects"]:
    #     print(item["rate"], item["title"])
    # print(type(citylist))
    # print(citylist)
    # content = json.dumps(citylist, ensure_ascii=False)
    # for item in hjson["results"]:
    #     print(item[""])
    # fp = open('city.json', 'w', encoding='UTF-8')
    # fp.write(content)
    # fp.close()

    # for item in hjson["results"]:
    #     print(item["rate"], item["title"])
    #     # 列印每條電影的評分與標題
