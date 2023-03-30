// const quizForm = document.getElementById('quiz-form');
// const submitButton = document.getElementById('submit');

// function showResults() {
// 	const answerContainers = quizForm.querySelectorAll('.question');
// 	let numCorrect = 0;

// 	answerContainers.forEach((questionContainer, questionNumber) => {
// 		const selector = `input[name=question${questionNumber + 1}]:checked`;
// 		const userAnswer = (questionContainer.querySelector(selector) || {}).value;

// 		if (userAnswer === 'b') {
// 			numCorrect++;
// 			questionContainer.style.color = 'green';
// 		} else {
// 			questionContainer.style.color = 'red';
// 		}
// 	});

// 	const resultsContainer = document.getElementById('results');
// 	resultsContainer.innerHTML = `${numCorrect} out of ${answerContainers.length}`;

// 	if (numCorrect === answerContainers.length) {
// 		resultsContainer.style.color = 'green';
// 	} else {
// 		resultsContainer.style.color = 'red';
// 	}
// }

// submitButton.addEventListener('click', showResults);

// submitButton.addEventListener('click', (event) => {
// 	event.preventDefault();

// 	const answerContainers = quizForm.querySelectorAll('.question');
// 	let numCorrect = 0;

// 	answerContainers.forEach((questionContainer, questionNumber) => {
// 		const selector = `input[name=question${questionNumber + 1}]:checked`;
// 		const userAnswer = (questionContainer.querySelector(selector) || {}).value;

// 		if (userAnswer === 'b') {
// 			numCorrect++;
// 			questionContainer.style.color = 'green';
// 		} else {
// 			questionContainer.style.color = 'red';
// 		}
// 	});

// 	const scoreContainer = document.createElement('div');
// 	scoreContainer.classList.add('score');
// 	scoreContainer.innerHTML = `You answered ${numCorrect} out of ${answerContainers.length} questions correctly!`;

// 	quizForm.appendChild(scoreContainer);
// });




const quizForm = document.getElementById('quiz-form');
const submitButton = document.getElementById('submit');

function showResults() {
    const answerContainers = quizForm.querySelectorAll('.question');
    let numCorrect = 0;

    answerContainers.forEach((questionContainer, questionNumber) => {
        const selector = `input[name=question${questionNumber + 1}]:checked`;
        const userAnswer = (questionContainer.querySelector(selector) || {}).value;
        const correctAnswer = questionContainer.getAttribute('data-correct-answer');

        if (userAnswer === correctAnswer) {
            numCorrect++;
            questionContainer.classList.add('correct');
        } else {
            questionContainer.classList.add('incorrect');
        }

        // Show the correct answer
        const correctAnswerElement = questionContainer.querySelector('.correct-answer');
        correctAnswerElement.style.display = 'block';
    });

    const resultsContainer = document.getElementById('results');
    resultsContainer.innerHTML = `${numCorrect} out of ${answerContainers.length}`;

    if (numCorrect === answerContainers.length) {
        resultsContainer.classList.add('all-correct');
    } else {
        resultsContainer.classList.add('not-all-correct');
    }
}


submitButton.addEventListener('click', showResults);

submitButton.addEventListener('click', (event) => {
    event.preventDefault();

    const answerContainers = quizForm.querySelectorAll('.question');
    let numCorrect = 0;

    answerContainers.forEach((questionContainer, questionNumber) => {
        const selector = `input[name=question${questionNumber + 1}]:checked`;
        const userAnswer = (questionContainer.querySelector(selector) || {}).value;
        const correctAnswer = questionContainer.getAttribute('data-correct-answer');

        if (userAnswer === correctAnswer) {
            numCorrect++;
            questionContainer.style.color = 'green';
        } else {
            questionContainer.style.color = 'red';
        }
    });

    const scoreContainer = document.createElement('div');
    scoreContainer.classList.add('score');
    scoreContainer.innerHTML = `You answered ${numCorrect} out of ${answerContainers
