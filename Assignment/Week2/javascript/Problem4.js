
// node Problem4.js

/*
要求四 ( 請閱讀英文 )：演算法
Given an array of integers, show indices of the two numbers such that they add up to a
specific target. You can assume that each input would have exactly one solution, and you
can not use the same element twice.
*/

/* javascript yield(類似 return) 使用: 
1.https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Statements/function*
2.https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/yield
*/

function* range(start, end) {
    for (let i = start; i <= end; i++) {
        yield i; // 疊代i值並回傳
    }
    //console.log("i : " + i)
}

function twoSum(nums, target) {

    // your code here
    /*
    nums = list
    target = nums index add result
    */
    const length_ = nums.length
    const List_ = []
    var index1, index2


    for (i = 0; i <= length_; i++) {
        // 1.range(x,y) --> x的意思是從參數i+1個數開始, 這邊就是省略i的第一個數(不要2又再加一次2 以下面範例的參數為例)
        for (let j of range(i + 1, length_)) {
            if (nums[i] + nums[j] == target) {
                //console.log(target)
                //console.log(i)
                //console.log(j)
                index1 = i
                index2 = j

                // 2.append index1 & 2 value to array :
                List_.push(index1)
                List_.push(index2)
            }
        }
    }

    return List_
}
let result = twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9

// 3.test the others :
let result1 = twoSum([2, 11, 7, 15], 13);
let result2 = twoSum([2, 11, 7, 15], 17);
let result3 = twoSum([2, 11, 7, 15], 26);
let result4 = twoSum([2, 11, 7, 15], 18);
let result5 = twoSum([2, 11, 7, 15], 22);
console.log(result1); // [0,1]
console.log(result2); // [0,3]
console.log(result3); // [1,3]
console.log(result4); // [1,2]
console.log(result5); // [2,3]


