
// node Problem3.js

/*
要求三：演算法
找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
提醒：請勿更動題目中任何已經寫好的程式，不可以使用排序相關的內建函式。
*/

function maxProduct(nums) {

    // 請用你的程式補完這個函式的區塊

    // 氣泡排序法 : 
    // 1.大到小 
    function bubbleSort_big_to_small(array) {
        const length = array.length;
        for (let i = 0; i < length; i++) {
            for (let j = 0; j < length; j++) {
                if (array[j] < array[j + 1]) {
                    let temp = array[j]
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
    }
    // 2.小到大
    function bubbleSort_small_to_big(array) {
        const length = array.length;
        for (let i = 0; i < length; i++) {
            for (let j = 0; j < length; j++) {
                // 核心程式思維 
                if (array[j] > array[j + 1]) {
                    let temp = array[j] //數字交換
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
    }
    // 1.max : 
    var max = nums
    var max_ = Math.max(...max); // Grab the highest value in the list 
    bubbleSort_big_to_small(nums); // 
    //console.log("bubbleSort nums : " + nums);
    nums_copy = nums.slice()
    nums_copy.shift()
    //console.log(" nums shift : " + nums_copy)
    var max2_ = Math.max(...nums_copy);
    max_mul = max_ * max2_

    // 2.min(negative*negative) : 
    var min = nums
    var min_ = Math.min(...min);
    bubbleSort_small_to_big(nums);
    nums_copy2 = nums.slice()
    nums_copy2.shift()
    var min2_ = Math.min(...nums_copy2);
    min_mul = min_ * min2_

    // 3.Compare Higher : 
    if (max_mul > min_mul)
        console.log(max_mul)
    else
        console.log(min_mul)
}

maxProduct([5, 20, 2, 6]) // 得到 120
maxProduct([10, -20, 0, 3]) // 得到 30
maxProduct([-1, 2]) // 得到 -2
maxProduct([-1, 0, 2]) // 得到 0
maxProduct([-1, -2, 0]) // 得到 2


