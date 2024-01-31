const burger = document.querySelector('.burgerMenu');
const menuL = document.querySelector('.burgerMenuList');

burger.addEventListener("click", function() {
  burger.classList.toggle('burgerMenuClose');
  menuL.classList.toggle('burgerMenuListOpen');
});

menuL.addEventListener("click", function(){
  burger.classList.remove('burgerMenuClose');
  menuL.classList.remove('burgerMenuListOpen');
});