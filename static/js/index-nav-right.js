const carticonMenu = document.getElementById("cartIcon");
const right = document.getElementById("right-side");
const cartClose = document.getElementById("closeIconForCart");
const mobileMenu = document.querySelector(".main_____mobile___menu");

carticonMenu.addEventListener("click", cartIoconRightBar);
cartClose.addEventListener("click", cartCloseIcon);

function cartIoconRightBar() {
  right.classList.add("navClass1");
  document
    .querySelector(".admin____overlayyyy")
    .classList.add("show__adminOverlayyy");

}

function cartCloseIcon() {
  right.classList.remove("navClass1");
  document
    .querySelector(".admin____overlayyyy")
    .classList.remove("show__adminOverlayyy");
    mobileMenu.style.zIndex = "-100";

}

document.addEventListener("click", (event) => {
  if (event.target.closest("#closeIconForCart")) return;
  if (event.target.closest("#right-side")) return;

  if (event.target.classList[1] === "show__adminOverlayyy") {
    document
      .querySelector(".admin____overlayyyy")
      .classList.remove("show__adminOverlayyy");
      right.classList.remove("navClass1");
    mobileMenu.style.zIndex = "-100";



  }

});
