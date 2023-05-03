/*
- loop through the string looking for /[aeiou]/ 
- once we find the vowel, we can splice the string from the vowel to the end. 
- then reattach the beginning to the end + 'way' or 'ay'
- example smile splice(2) + splice(0,1) + 'ay' 'way'
*/
function piglatin(str) {
    let firstVowel = str.match(/[aeiou]/)
    let firstPos = str.indexOf(firstVowel)
    
   
   
   
   
    // console.log(firstPos)
    // console.log(firstVowel)

}
console.log(piglatin('smile'))