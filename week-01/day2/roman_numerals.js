function toRoman(num) {
    let str = '';
    let roman_numerals = {
        M: 1000,
        D: 500,
        C: 100,
        L: 50,
        X: 10,
        V: 5,
        I: 1
    }
    for (key in roman_numerals) {
    while (num >= roman_numerals[key]) {
        str = str + key
        num -= roman_numerals[key]
    }
    }
    return str
}
console.log(toRoman(1201))