# 要求四：SQL Aggregate Functions

# 4.1 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
SELECT COUNT(test2) FROM member;

# 4.2 取得 member 資料表中，所有會員 follower_count 欄位的總和。
SELECT SUM(follower_count) FROM member;

# 4.3 取得 member 資料表中，所有會員 follower_count 欄位的平均數
SELECT AVG(follower_count) FROM member;

# 4.4 MAX & MIN : Extra(額外)
SELECT MAX(follower_count) FROM member;
SELECT MIN(follower_count) FROM member;
# ====================================== #
