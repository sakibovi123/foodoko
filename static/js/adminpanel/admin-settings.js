const image = document.querySelector(".after___new___upload");
const two = document.querySelector(".two____btn");
const twoFav = document.getElementById("two-btn-fav");
const twostore = document.getElementById("two-btn-store");
const twodri = document.getElementById("two-btn-dri");
const twoem = document.getElementById("two-btn-em");


const selectImage = document.querySelector(".final____select");
const cancelBtn = document.querySelector(".cancel____btn__pro");
const favcancel = document.querySelector(".fav-cancel");
const storecancel = document.querySelector(".store-cancel");
const dricancel = document.querySelector(".dri-cancel");

const emcancel = document.querySelector(".em-cancel");


const favicon = document.querySelector(".select-fav");
const storeicon = document.querySelector(".select-store");
const driicon = document.querySelector(".select-dri");

const emicon = document.querySelector(".select-em");


const image1 = document.getElementById("product__img-drive");
const imagestore = document.getElementById("product__img-store");
const imagedri = document.getElementById("product__img-dri");

const imageem = document.getElementById("product__img-em");


const favSelect = document.getElementById("fav-select-image");
const storeSelect = document.getElementById("store-select-image");
const driSelect = document.getElementById("dri-select-image");

const emSelect = document.getElementById("em-select-image");



const existImg = document.getElementById("main-images-fav");
const existImgstore = document.getElementById("main-images-store");
const existImgdri = document.getElementById("main-images-dri");

const existImgem = document.getElementById("main-images-em");


const favImg = document.getElementById("product__img-drive");
const storeImg = document.getElementById("product__img-store");
const driImg = document.getElementById("product__img-dri");

const emImg = document.getElementById("product__img-em");



image.style.display = "none"
two.style.display = "none";
twoFav.style.display = "none";
twostore.style.display = "none";
twodri.style.display = "none";

twoem.style.display = "none";


cancelBtn.addEventListener("click", cancelBtnClick);
favcancel.addEventListener("click", favCancelBtn);
storecancel.addEventListener("click", storeCancelBtn);
dricancel.addEventListener("click", driCancelBtn);

emcancel.addEventListener("click", emCancelBtn);



// favicon.addEventListener("change", favChange);
// storeicon.addEventListener("change", storeChange);


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
    document.querySelector(".main-images-fav").style.display = "none";
    image.style.display = "block"
    }
    }

    function favCancelBtn(){
      document.querySelector("#product__img-drive").style.display = "none";
existImg.style.display = "flex";
twoFav.style.display = "none";
favSelect.style.display = "block";
    } 



// store js

imagestore.style.display = "none";

  function foruploadstore(e) {
    let fileVal = e.files[0];

    if (fileVal) {
      document.querySelector("#product__img-store").src = URL.createObjectURL(fileVal);
      existImgstore.style.display = "none";
      imagestore.style.display = "flex";
      twostore.style.display = "flex";
      storeSelect.style.display = "none"

    }
  }

  function foruploadchangestore(e) {
    let fileVal = e.files[0];
    
    if (fileVal) {
    document.querySelector("#product__img-store").src = URL.createObjectURL(fileVal);
    document.querySelector(".main-images-store").style.display = "none";
    image.style.display = "block"
    }
    }

    function storeCancelBtn(){
      document.querySelector("#product__img-store").style.display = "none";
      existImgstore.style.display = "flex";
twostore.style.display = "none";
storeSelect.style.display = "block";
    } 




// email js

imageem.style.display = "none";

  function foruploadem(e) {
    let fileVal = e.files[0];

    if (fileVal) {
      document.querySelector("#product__img-em").src = URL.createObjectURL(fileVal);
      existImgem.style.display = "none";
      imageem.style.display = "flex";
      twoem.style.display = "flex";
      emSelect.style.display = "none"

    }
  }

  function foruploadchangeem(e) {
    let fileVal = e.files[0];
    
    if (fileVal) {
    document.querySelector("#product__img-em").src = URL.createObjectURL(fileVal);
    document.querySelector(".main-images-em").style.display = "none";
    image.style.display = "block"
    }
    }

    function emCancelBtn(){
      document.querySelector("#product__img-em").style.display = "none";
      existImgem.style.display = "flex";
twoem.style.display = "none";
emSelect.style.display = "block";
    }     


    
// driver js

imagedri.style.display = "none";

function foruploaddri(e) {
  let fileVal = e.files[0];

  if (fileVal) {
    document.querySelector("#product__img-dri").src = URL.createObjectURL(fileVal);
    existImgdri.style.display = "none";
    imagedri.style.display = "flex";
    twodri.style.display = "flex";
    driSelect.style.display = "none"

  }
}

function foruploadchangedri(e) {
  let fileVal = e.files[0];
  
  if (fileVal) {
  document.querySelector("#product__img-dri").src = URL.createObjectURL(fileVal);
  document.querySelector(".main-images-dri").style.display = "none";
  image.style.display = "block"
  }
  }

  function driCancelBtn(){
    document.querySelector("#product__img-dri").style.display = "none";
    existImgdri.style.display = "flex";
twodri.style.display = "none";
driSelect.style.display = "block";
  }     