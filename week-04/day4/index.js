const btn = document.querySelector("#btn");

function replaceimages() {
  const nodelist = document.body.querySelectorAll(".img");

  // nodelist.forEach(img => console.log(img.alt))
  let images = document.body.getElementsByTagName("img");
  console.log(nodelist);
  console.log(images);
  for (let i = images.length - 1; i >= 0; i--) {
    let image = images[i];
    if (image.alt) {
      let text = document.createTextNode(image.alt);
      image.parentNode.replaceChild(text, image);
    }
  }
}
