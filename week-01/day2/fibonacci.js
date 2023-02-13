function fibonacci(num) {
    let arr = [0,1];
    let count = 0;
    let first = 0
    let second = 1
    while (num >= count) {
        let temp = first + second;
        first = second
        second = temp
        count++
        arr.push(temp)
    }
    return console.log(arr[num - 1])
}
fibonacci(8)