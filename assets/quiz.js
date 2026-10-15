// quiz.js — instant-feedback quiz widget. Vanilla JS, no dependencies.
//
// Expected markup, one block per lesson:
//
//   <section class="quiz" id="quiz">
//     <h2>Quiz</h2>
//     <ol class="quiz-questions">
//       <li class="quiz-question" data-correct="b">
//         <p class="quiz-stem">Question text?</p>
//         <ul class="quiz-options">
//           <li><button type="button" data-option="a">First option</button></li>
//           <li><button type="button" data-option="b">Second option</button></li>
//         </ul>
//         <p class="quiz-feedback" hidden></p>
//         <p class="quiz-explain" hidden>Why the answer is right.</p>
//       </li>
//     </ol>
//     <p class="quiz-score" hidden></p>
//   </section>
//
// Behavior: the learner clicks one option per question. The widget shows
// right or wrong at once, reveals the explanation, and locks the question.
// When every question is answered, the widget shows the score.

(function () {
  'use strict';

  function answerQuestion(question, button, state) {
    var correct = question.getAttribute('data-correct');
    var chosen = button.getAttribute('data-option');
    var isCorrect = chosen === correct;

    question.querySelectorAll('.quiz-options button').forEach(function (b) {
      b.disabled = true;
      if (b.getAttribute('data-option') === correct) {
        b.classList.add('correct');
      }
    });
    if (!isCorrect) {
      button.classList.add('incorrect');
    }

    var feedback = question.querySelector('.quiz-feedback');
    if (feedback) {
      feedback.textContent = isCorrect
        ? 'Correct.'
        : 'Not quite. The marked option is the answer.';
      feedback.classList.add(isCorrect ? 'is-correct' : 'is-incorrect');
      feedback.hidden = false;
    }

    var explain = question.querySelector('.quiz-explain');
    if (explain) {
      explain.hidden = false;
    }

    state.answered += 1;
    if (isCorrect) {
      state.correct += 1;
    }
    if (state.answered === state.total && state.scoreEl) {
      state.scoreEl.textContent =
        'Score: ' + state.correct + ' of ' + state.total + '.';
      state.scoreEl.hidden = false;
    }
  }

  function initQuiz(quiz) {
    var questions = quiz.querySelectorAll('.quiz-question');
    var state = {
      total: questions.length,
      answered: 0,
      correct: 0,
      scoreEl: quiz.querySelector('.quiz-score')
    };

    questions.forEach(function (question) {
      question.querySelectorAll('.quiz-options button').forEach(function (button) {
        button.addEventListener('click', function () {
          answerQuestion(question, button, state);
        });
      });
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.quiz').forEach(initQuiz);
  });
})();
