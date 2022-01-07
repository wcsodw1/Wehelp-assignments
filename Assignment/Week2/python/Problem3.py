
# python Problem3.py

'''
要求三：演算法
找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
提醒：請勿更動題目中任何已經寫好的程式，不可以使用排序相關的內建函式。
'''


def max2(x):
    m1 = max(x)  # m1是最大元素
    x2 = x.copy()  # 复制一个列表，同时不破坏原来的列表
    x2.remove(m1)  # 把列表里最大的元素删除
    m2 = max(x2)  # 再次取列表里最大的元素，这时取到的就是列表里第二大的元素
    return m2, m1  # m1是第二大的值,m2是最大值


def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊

    max_ = sec_max = None

    # 1.Plus
    #   a.max value :
    for num in nums:
        if (max_ is None or num > max_):
            max_ = num
    cut_max = nums.copy()  # copy the list
    cut_max.remove(max_)  # remove max

    #   b.Second max value :
    for num in cut_max:
        if (sec_max is None or num > sec_max):
            sec_max = num
    result_plus = max_*sec_max

    # 2.Negative multiple :

    # a.min value:
    for i in nums:
        min_ = min(nums)
    cut_min = nums.copy()  # 复制一个列表，同时不破坏原来的列表
    cut_min.remove(min_)  # 把列表里最大的元素删除

    #   b.Second min value :
    for i in cut_min:
        sec_min = min(cut_min)

    result_neg = min_*sec_min

    if result_plus > result_neg:
        print(result_plus)

    else:
        print(result_neg)


maxProduct([5, 20, 2, 6])  # 得到 120
maxProduct([10, -20, 0, 3])  # 得到 30
maxProduct([-1, 2])  # 得到 -2
maxProduct([-1, 0, 2])  # 得到 0
maxProduct([-1, -2, 0])  # 得到 2
