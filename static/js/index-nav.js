const menu = document.getElementById("burger____menu");
const firstSide = document.getElementById("first-side");
const closeMenu = document.getElementById("close");
const total = document.getElementById("hello1");


menu.addEventListener("click", menuFunc);
closeMenu.addEventListener("click", closeIocn);

function menuFunc() {
  firstSide.classList.add("navClass");
  document
    .querySelector(".admin____overlay")
    .classList.add("show__adminOverlay");

  total.style.zIndex = "-1";
}

function closeIocn() {
  firstSide.classList.remove("navClass");
  document
    .querySelector(".admin____overlay")
    .classList.remove("show__adminOverlay");

  total.style.zIndex = "-1";
}

document.addEventListener("click", (event) => {
  if (event.target.closest("#close")) return;
  if (event.target.closest("#first-side")) return;

  if (event.target.classList[1] === "show__adminOverlay") {
    document
      .querySelector(".admin____overlay")
      .classList.remove("show__adminOverlay");
    firstSide.classList.remove("navClass");
    total.style.zIndex = "-1";
  }
});
