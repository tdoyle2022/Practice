function linearSearch(item, arr) {
    for (item of arr) {
        if (arr.indexOf(arr[item]) === -1) {
            return ''
        }
        console.log(arr.indexOf(arr[item]))
    }
}
linearSearch(3, [2,3,4])

function globalLinearSearch(item, arr) {
    
}