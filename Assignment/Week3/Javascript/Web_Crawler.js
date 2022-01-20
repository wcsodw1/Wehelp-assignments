
// node Web_Crawler.js

const Nightmare = require('nightmare');          // 自動化測試包，處理動態頁面
const nightmare = Nightmare({ show: true });     // show:true  顯示內建模擬瀏覽器
/**
* [description] - 抓取本地新聞頁面
* [nremark] - 百度本地新聞在訪問頁面後載入js定位IP位置後獲取對應新聞，
* 所以抓取本地新聞需要使用 nightmare 一類的自動化測試工具，
* 模擬瀏覽器環境訪問頁面，使js執行，生成動態頁面再抓取
*/
// 抓取本地新聞頁面
nightmare
    // .goto('http://news.baidu.com/')
    .goto('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json')
    .wait("div#local_news")
    .evaluate(() => document.querySelector("div#local_news").innerHTML)
    .then(htmlStr => {
        // 獲取本地新聞資料
        localNews = getLocalNews(htmlStr)
    })
    .catch(error => {
        console.log(`本地新聞抓取失敗 - ${error}`);
    })