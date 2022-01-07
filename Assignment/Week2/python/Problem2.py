
# python Problem2.py

'''
要求二：Python 字典與列表、JavaScript 物件與陣列
完成以下函式，正確計算出員工的平均薪資，請考慮員工數量會變動的情況。
提醒：請勿更動題目中任何已經寫好的程式。
(!) 這邊字典有加入list 元素
'''

# 1.Algorithm :


def avg(data):
    # 請用你的程式補完這個函式的區塊

    # 1.先get出第一維度的資料, 在對它裡面做事
    employees = data.get('employees')
    sum = length = 0

    # 2.取dict key中的資料
    for i in employees:
        # print(i['salary'])
        salary = i['salary']  # 取出dictinary key(employees)中的 value值
        sum = sum+salary  # summaztion of salary
        length = length+1  # 計算salary總資料數

    avg = sum/length  # calculate the average salary
    print("Sum = ", sum)
    print("Length : ", length)
    print("Average Salary = ", avg)


# 2.呼叫 avg 函式 :
avg({
    "count": 3,
    "employees": [
        {
            "name": "John",
            "salary": 30000
        },

        {
            "name": "Bob",
            "salary": 60000
        },

        {
            "name": "Jenny",
            "salary": 50000
        }
    ]
})

""" Output : """
# Sum =  140000
# Length :  3
# Average Salary =  46666.666666666664
