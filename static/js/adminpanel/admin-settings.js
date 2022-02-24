const image = document.querySelector(".after___new___upload");
const two = document.querySelector(".two____btn");
const twoFav = document.getElementById("two-btn-fav");
const selectImage = document.querySelector(".final____select");
const cancelBtn = document.querySelector(".cancel____btn__pro");
const favcancel = document.querySelector(".fav-cancel");
const favicon = document.querySelector(".select-fav");
const image1 = document.getElementById("product__img-drive");
const favSelect = document.getElementById("fav-select-image");

const existImg = document.getElementById("main-images-fav");
const favImg = document.getElementById("product__img-drive");

image.style.display = "none"
two.style.display = "none";
twoFav.style.display = "none";
cancelBtn.addEventListener("click", cancelBtnClick);
favcancel.addEventListener("click", favCancelBtn);
favicon.addEventListener("change", favChange);


function forupload(e) {
let fileVal = e.files[0];

if (fileVal) {
image.src = URL.createObjectURL(fileVal);
document.querySelector(".main-images-pro").style.display = "none";
image.style.display = "block"
two.style.display = "flex";
selectImage.style.display = "none";
}
}

function foruploadchange(e) {
let fileVal = e.files[0];

if (fileVal) {
image.src = URL.createObjectURL(fileVal);
document.querySelector(".main-images-pro").style.display = "none";
image.style.display = "block"
}
}
function cancelBtnClick(){
two.style.display = "none";
image.style.display = "none";
document.querySelector(".main-images-pro").style.display = "flex";
selectImage.style.display = "block";
}


// fav js
  image1.style.display = "none";

  function foruploaddrive(e) {
    let fileVal = e.files[0];

    if (fileVal) {
      document.querySelector("#product__img-drive").src = URL.createObjectURL(fileVal);
      existImg.style.display = "none";
      image1.style.display = "flex";
      twoFav.style.display = "flex";
      favSelect.style.display = "none"

    }
  }

  function foruploadchangeFav(e) {
    let fileVal = e.files[0];
    
    if (fileVal) {
    document.querySelector("#product__img-drive").src = URL.createObjectURL(fileVal);
    document.querySelector(".main-images-pro").style.display = "none";
    image.style.display = "block"
    }
    }

    function favCancelBtn(){
      document.querySelector("#product__img-drive").style.display = "none";
existImg.style.display = "flex";
twoFav.style.display = "none";
favSelect.style.display = "block";
    } 
