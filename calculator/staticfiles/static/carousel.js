document.addEventListener("DOMContentLoaded", function () {
    const carouselContainer = document.querySelector(".ourCars ul");
    const carouselItems = document.querySelectorAll(".ourCars ul li");
    const arrowBack = document.querySelector(".arrowBack");
    const arrowForward = document.querySelector(".arrowForward");
    let currentIndex = 0;
    const totalItems = carouselItems.length;

    arrowForward.addEventListener("click", function () {
      currentIndex++;
      if (currentIndex >= totalItems) {
        currentIndex = 0;
      }
      const newPosition = -currentIndex * 20;
      carouselContainer.style.transform = `translateX(${newPosition}%)`; // Use translateX() for X-direction
    });

    arrowBack.addEventListener("click", function () {
      currentIndex--;
      if (currentIndex < 0) {
        currentIndex = totalItems - 1;
      }
      const newPosition = -currentIndex * 20;
      carouselContainer.style.transform = `translateX(${newPosition}%)`; // Use translateX() for X-direction
    });
  });