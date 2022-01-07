
# python Problem5.py

'''
要求五 ( Optional )：演算法
給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大
長度。
提醒：請勿更動題目中任何已經寫好的程式。

'''


def maxZeros(nums):
    target = 0  # target : 將要計算連續的值(可自由設定)
    add = 0  # 計步值(累積增加)
    sum = 0

    # Loop the list
    for i in nums:
        # 變數值若等於目標值 :
        if i == target:
            add += 1  # 累加變數值數量
            # 若add儲存(copy)累加值到sum變數
            if sum < add:
                sum = add
                print("sum", sum)
        else:
            add = 0
    print(nums, "最大連續0的數為 : ", sum)
    print("============================")


# 請用你的程式補完這個函式的區塊
maxZeros([0, 1, 0, 0])  # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])  # 得到 4
maxZeros([1, 1, 1, 1, 1])  # 得到 0
maxZeros([0, 0, 0, 1, 1])  # 得到 3
maxZeros([0, 0, 0, 0, 0])  # 5
