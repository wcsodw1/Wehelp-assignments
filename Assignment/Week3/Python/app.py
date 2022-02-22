
# python app.py
import csv
import json
import urllib.request as req

url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")


data = json.loads(data)
data = data["result"]["results"]


header = ['景點名稱', '區域', '經度', '緯度', '第一張圖檔網址']
# csv data
rows = []
# open the file in the write mode
with open("data.csv", "w", newline="") as csvfile:
    # create the csv writer
    writer = csv.writer(csvfile)

    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()

    for post in data:
        # writer.writerows(rows)
        writer.writerow({
            '景點名稱': post["stitle"],
            '區域': post["address"].split(" ")[2][0:3],
            '經度': post["longitude"],
            '緯度': post["latitude"],
            '第一張圖檔網址': post["file"].lower().partition(".jpg")[0]+".jpg"
        })
