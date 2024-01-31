
function startCountAnimationOnScroll() {
    const counts = document.querySelectorAll('.num');
    const speed =4330;
    let animationStarted = false;

    function upData() {
      counts.forEach((counter) => {
        const target = Number(counter.getAttribute('data-target'));
        const count = Number(counter.innerText);
        let inc;

        if (target > count) {
          inc = Math.ceil((target - count) / speed); // Adjust the inc value
          counter.innerText = count + inc > target ? target : count + inc;
        } else {
          inc = Math.ceil((count - target) / speed); // Adjust the inc value
          counter.innerText = count - inc < target ? target : count - inc;
        }

        if (count !== target) {
          setTimeout(upData, 1);
        }
      });
    }

    function handleIntersect(entries, observer) {
      entries.forEach((entry) => {
        if (entry.isIntersecting && !animationStarted) {
          animationStarted = true;
          upData();
          observer.unobserve(entry.target); // Stop observing once animation starts
        }
      });
    }

    const observer = new IntersectionObserver(handleIntersect, { threshold: 0 });

    counts.forEach((counter) => {
      observer.observe(counter);
    });
  }

  // Call the function to start the counting animation on scroll
  startCountAnimationOnScroll();