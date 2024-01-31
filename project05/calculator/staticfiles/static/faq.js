

// Get all the question elements
const questions = document.querySelectorAll('.question');

// Add a click event listener to each question
questions.forEach(question => {
  question.addEventListener('click', function() {
    // Toggle the "active" class on the associated answer element
    const answer = this.nextElementSibling;
    answer.classList.toggle('active');

    // Get the arrowImg element for the current question
    const arrowImg = this.querySelector('.arrowImg');

    // Add the animation class to arrowImg based on whether the answer is active or not
    if (answer.classList.contains('active')) {
      arrowImg.classList.remove('rotateDown');
      arrowImg.classList.add('rotate');
    } else {
      arrowImg.classList.add('rotateDown');
      arrowImg.classList.remove('rotate');
    }
  });
});