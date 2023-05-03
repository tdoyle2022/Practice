const btn = document.querySelector("#btn");
num = 0
btn.addEventListener("click", (evt) => {
    getimg()})

function random() {
        rannum = Math.floor(Math.random() * 100) + 1;
        rannum = num;
    return num
}
random()
function getimg() {
    axios.get(`https://pokeapi.co/api/v2/pokemon/${random()}`)
    .then(response => {
    let imageURL = response.data.sprites.front_default
    console.log(imageURL)
    
    let image_element = document.createElement('img')

    image_element.src = imageURL
    document.body.appendChild(image_element)
})
}
