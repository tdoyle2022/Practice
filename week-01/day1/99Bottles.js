function bottles(num) {
  if (num <=0) {
    console.log("No more bottles of beer on the wall, no more bottles of beer. \n Go to the store and buy some more, 99 bottles of beer on the wall.")
  }
  if (num == 2) {
    console.log(`${num} bottles of beer on the wall, ${num} bottles of beer. \n Take one down and pass it around, ${num -1} bottle of beer on the wall.`)
    return bottles(num-1)}
  while (num >= 3) {
    console.log(`${num} bottles of beer on the wall, ${num} bottles of beer. \n Take one down and pass it around, ${num -1} bottles of beer on the wall.`)
    return bottles(num - 1)
  }
}
bottles(99)