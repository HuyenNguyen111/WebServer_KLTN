const path = document.location.pathname;
const itemMenu = document.querySelectorAll(".menu-item");
console.log(itemMenu);
if (path.match("/history/.*")) {
    itemMenu[1].classList.add("active");
} else {
    itemMenu[0].classList.add("active");
}
