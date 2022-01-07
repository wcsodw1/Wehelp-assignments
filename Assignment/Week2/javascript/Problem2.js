
// node Problem2.js

/*
要求二：Python 字典與列表、JavaScript 物件與陣列
完成以下函式，正確計算出員工的平均薪資，請考慮員工數量會變動的情況。
提醒：請勿更動題目中任何已經寫好的程式。
*/

function avg(data) {
    // 請用你的程式補完這個函式的區塊

    // 1.先get出第一維度的資料, 在對它裡面做事
    var employees = data["employees"]
    var salary, sum = 0, length = 0, avg // declare sum = 0 before calculate
    console.log(employees)

    // 2.取dict key中的資料
    for (const value of Object.values(employees)) {
        //console.log(value['salary'])
        salary = value['salary'] // 取出dictinary key(employees)中的 value值
        var sum = sum + salary // summaztion of salary
        //console.log(sum) 
        length = length + 1 // 計算salary總資料數
    }
    avg = sum / length // calculate the average salary
    console.log("Sum = " + sum)
    console.log("length = " + length)
    console.log("Average = " + avg)

}
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
}); // 呼叫 avg 函式

