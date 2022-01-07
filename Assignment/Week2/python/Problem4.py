
# python Problem4.py

'''
要求四 ( 請閱讀英文 )：演算法
Given an array of integers, show indices of the two numbers such that they add up to a
specific target. You can assume that each input would have exactly one solution, and you
can not use the same element twice.

'''


def twoSum(nums, target):

    # your code here
    '''
    nums = list
    target = nums index add result
    '''

    length = len(nums)
    List_ = []
    for i in range(length):
        # 1.range(x,y) --> x的意思是從參數i+1個數開始, 這邊就是省略i的第一個數(不要2又再加一次2 以下面範例的參數為例)
        for j in range(i+1, length):
            if nums[i] + nums[j] == target:
                index1 = i  # index1
                index2 = j  # index2
                # print(i)
                # print(j)
                # 2.append index1 & 2 value to array :
                List_.append(index1)
                List_.append(index2)  # add index2 to array
                #print("List_ : ", List_)

    return List_


result = twoSum([2, 11, 7, 15], 9)
# show [0, 2] because nums[0]+nums[2] is 9
print("Target 9 index is : ", result)


# 3.test the others :
result1 = twoSum([2, 11, 7, 15], 13)
result2 = twoSum([2, 11, 7, 15], 17)
result3 = twoSum([2, 11, 7, 15], 26)
result4 = twoSum([2, 11, 7, 15], 18)
result5 = twoSum([2, 11, 7, 15], 22)
print("Target 13 index is : ", result1)  # [0,1]
print("Target 17 index is : ", result2)  # [0,3]
print("Target 26 index is : ", result3)  # [1,3]
print("Target 18 index is : ", result4)  # [1,2]
print("Target 22 index is : ", result5)  # [2,3]
