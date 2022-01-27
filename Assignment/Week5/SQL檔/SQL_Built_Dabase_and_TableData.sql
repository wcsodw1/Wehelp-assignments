# MySQL基本指令 : - (!) \! cls # clear(clean) MySQL

# 1.連線到資料庫 : ("root"為資料庫密碼) - mysql -u root -p
# 2.建立資料庫 :  (`website` 為創建資料庫的名稱, (!) 旁邊括號是`, 而不是'- CREATE DATABASE `website`;
# 3.選擇建立的資member_料庫 : - use website;
# 4.建立會員資料表 :
use website; # 使用自己剛創建的website資料庫
CREATE TABLE member (  # 新增會員資料表
id INT NOT NULL AUTO_INCREMENT, # 1.id :會員ID 2.AUTO_INCREMENT:自動累加, 3.用途說明 : 會員的獨立編號
name varchar(255) NOT NULL,  # (!)用途說明 name : 會員名字 2.NOT NULL : 此欄不可為空值 3.varchar(255):資料型態
username varchar(255) NOT NULL,  # (!)用途說明 username : 帳戶名稱 2.NOT NULL(同上) 3.varchar(255):(同上)
password varchar(255) NOT NULL,  # (!)用途說明 password : 帳戶密碼 2.NOT NULL(同上) 3.varchar(255):(同上)
follower_count INT NOT NULL,  # (!)用途說明 follower_count : 追蹤者數量 2.INT:不可為空值，預設為0 3.NOT NULL(同上)
time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, # (!)用途說明 time : 註冊時間 1.follower_count : 追蹤者數量 2.2.NOT NULL(同上) 3.DEFAULT CURRENT_TIMESTAMP : 自動初始化: 資料寫入欄位，自動填入當下時間
PRIMARY KEY(id) #  (!)用途說明 PRIMARY KEY(id) : 藉由id的設定以便能撈到想要資料
);

-- INSERT INTO date_test (name, last_update1, last_update2)
-- VALUES ("test1", NOW(), CURDATE());
# 5.刪除整個(member)資料表 : - 
-- DROP TABLE member_;
