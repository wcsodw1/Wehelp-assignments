# 要求三 : CRUD(Create, Retrieve, Update, Delete)

#=========== PART A : INSERT =============# 
# 3.1 使用 INSERT 指令新增資料 : 
# 	A.輸入單一筆資料 :
INSERT INTO member (id, name, username, password, follower_count, time)
VALUES (2, 'EstherLu','Esther', 'Lu', 1000, Now());

INSERT INTO member
VALUES (1, 'DavidLin','test', 'test', 500, Now());

INSERT INTO member 
VALUES (3, 'Wayne_Wu_Please','Wayne', 'Wu', 1000, Now());

INSERT INTO member 
VALUES  (4, 'Jacky_Jiang','jacky', 'Jiang', 1000, Now());

INSERT INTO member 
VALUES  (5, 'Bobby','rob', 'scientist', 800, Now());

INSERT INTO member 
VALUES  (6, 'Jane','single', 'needMan', 600, Now());

#	B.輸入多筆資料 : 
INSERT INTO member_ (id, name, username, password, follower_count, time)
VALUES (1, 'DavidLin','test', 'test', 500, Now()), # Now() = CURRENT_TIMESTAMP()
(2, 'EstherLu','Esther', 'Lu', 1000, Now()), 
(3, 'Wayne_Wu_Please','Wayne', 'Wu', 1000, Now()),
(4, 'Jacky_Jiang','jacky', 'Jiang', 1000, Now()),
(5, 'Bobby','rob', 'scientist', 800, Now()),
(6, 'Jane','single', 'needMan', 600, Now());

# 	C.清除Table內值(ex:member_) : 若鍵錯檔案, 可以刪除資料在重建
DELETE FROM member;
# 	D. 清除某特定Column資料 : 
DELETE FROM member WHERE column_name username value;

#=========== PART B : SELECT & UPDATE =============# 
# 3.2 : 使用 SELECT 指令取得所有在 member 資料表中的會員資料。
SELECT * FROM member_;

# 3.使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
select * from member order by time asc;
select * from member order by time desc;

# 4.使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
select * from member order by time asc;
select * from member order by time asc LIMIT 1,3;

# (!)Extra(額外) : 若使用id順序的方法
select * from member WHERE id in (2, 3, 4);

# 5.使用 SELECT 指令取得欄位 username 是 test 的會員資料。
select * from member WHERE username="test";

# 6.使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
select * from member WHERE username ="test" AND password ="test";

# 7.使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
ALTER TABLE member RENAME COLUMN name TO test2;