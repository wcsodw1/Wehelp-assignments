
// node Problem2.js

/*
要求五 ( Optional )：演算法
給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大
長度。
提醒：請勿更動題目中任何已經寫好的程式。
*/

function maxZeros(nums) {
    // 請用你的程式補完這個函式的區塊
    var target = 0
    var add = 0
    var sum = 0
    const length = nums.length;
    //console.log("nums : " + nums)
    //console.log("nums length : " + length)

    for (i = 0; i <= nums.length; i++) {
        if (nums[i] == target) {
            //console.log("i = " + i)
            add = add + 1
            //console.log("add : " + add)
            if (sum < add) {
                sum = add
                //console.log("sum = " + sum)
            }
        }
        else
            add = 0
    }

    console.log(nums, "最大連續0的數為 : ", sum)
    console.log("============================")


}
maxZeros([0, 1, 0, 0]); // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
maxZeros([1, 1, 1, 1, 1]); // 得到 0
maxZeros([0, 0, 0, 1, 1]) // 得到 3
maxZeros([0, 0, 0, 0, 0]) // 得到 5