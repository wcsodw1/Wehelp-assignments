

# WEeek5 MySQL : 

## 要求三：SQL CRUD : 

### 3.2 : 使用 SELECT 指令取得所有在 member 資料表中的會員資料。
cmd : SELECT * FROM member; <br>
 ![image](./img/Task3-2_selectTableTotalData.PNG)

### 3.3 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
- A.近到遠 : 
cmd : select * from member order by time asc;
 ![image](./img/Task3-3_selectDatabyTimeASC.PNG)

- B.遠到近 : 
cmd : select * from member order by time desc;
 ![image](./img/Task3-3_selectDatabyTimeDESC.PNG)

### 3.4 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
cmd : select * from member order by time asc LIMIT 1,3;
 ![image](./img/Task3-4_select2-4DatabyTime.PNG)

#### (!)Extra(額外) : 若使用id順序的方法
cmd : select * from member WHERE id in (2, 3, 4);
 ![image](./img/Task3-4_select2-4DatabyID.PNG)

### 3.5 使用 SELECT 指令取得欄位 username 是 test 的會員資料。
cmd : select * from member WHERE username="test";
 ![image](./img/Task3-5_selectColumnValue.PNG)

### 3.6 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
cmd : select * from member WHERE username ="test" AND password ="test";
 ![image](./img/Task3-6_selectColumnMultiValue.PNG)

### 3.7 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
cmd : ALTER TABLE member RENAME COLUMN name TO test2;
 ![image](./img/Task3-7_updateColumnNamebyRENAME.PNG)


## 要求四：SQL Aggregate Functions : 

### 4.1 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
cmd : SELECT COUNT(test2) FROM member;

### 4.2 取得 member 資料表中，所有會員 follower_count 欄位的總和。
cmd : SELECT SUM(follower_count) FROM member;

### 4.3 取得 member 資料表中，所有會員 follower_count 欄位的平均數
cmd : SELECT AVG(follower_count) FROM member;<br>
  ![4-1~4-3](./img/Task4_1-3_count_sum_avg_MemberNumber.PNG)

### 4.4, 4.5 MAX & MIN : Extra(額外)
SELECT MAX(follower_count) FROM member;
SELECT MIN(follower_count) FROM member;<br>
 ![image](./img/Task4_4-5countMemberNumber.PNG)
 
## 要求五：SQL JOIN (Optional) :