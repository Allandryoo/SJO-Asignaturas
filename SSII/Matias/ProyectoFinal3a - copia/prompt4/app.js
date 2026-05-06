const appState = {
  questions: [],
  currentIndex: 0,
  score: 0,
  categoryStats: {},
  isStarted: false,
  isFinished: false
};

const App = {
  container: null,

  init(questionsData) {
    this.container = document.getElementById('app-container');
    if (!this.container) {
      console.error('Contenedor app #app-container no encontrado');
      return;
    }

    appState.questions = this.shuffleArray([...questionsData]);
    this.initCategoryStats();
    this.bindEvents();
    this.renderWelcomeScreen();
  },

  initCategoryStats() {
    const categories = ["Comandos Windows", "Comandos Linux", "Hardware", "Redes IP", "Contenedores"];
    categories.forEach(cat => {
      appState.categoryStats[cat] = { correct: 0, total: 0 };
    });
  },

  shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  },

  bindEvents() {
    this.container.addEventListener('click', (e) => this.handleClick(e));
  },

  handleClick(e) {
    if (e.target.id === 'start-btn' && !appState.isStarted) {
      this.startTest();
    } else if (e.target.classList.contains('option-btn') && !appState.isFinished) {
      this.handleAnswer(e.target);
    } else if (e.target.id === 'restart-btn') {
      this.restartTest();
    }
  },

  renderWelcomeScreen() {
    appState.isStarted = false;
    appState.isFinished = false;
    this.container.innerHTML = createWelcomeScreen(
      'Autoescuela de Sistemas',
      'Pon a prueba tus conocimientos de hardware y sistemas'
    );
  },

  startTest() {
    appState.isStarted = true;
    appState.currentIndex = 0;
    appState.score = 0;
    this.initCategoryStats();
    this.renderQuestion();
  },

  renderQuestion() {
    const question = appState.questions[appState.currentIndex];
    const progressBar = createProgressBar(appState.currentIndex + 1, appState.questions.length);
    const questionCard = createQuestionCard(question);

    this.container.innerHTML = progressBar + questionCard;
  },

  handleAnswer(selectedButton) {
    const question = appState.questions[appState.currentIndex];
    const selectedOption = selectedButton.dataset.option;
    const isCorrect = selectedOption === question.correctAnswer;

    const buttons = this.container.querySelectorAll('.option-btn');
    buttons.forEach(btn => {
      btn.disabled = true;
      if (btn.dataset.option === question.correctAnswer) {
        btn.classList.add('correct');
      } else if (btn === selectedButton && !isCorrect) {
        btn.classList.add('incorrect');
      }
    });

    const category = question.category;
    appState.categoryStats[category].total++;
    if (isCorrect) {
      appState.score++;
      appState.categoryStats[category].correct++;
    }

    setTimeout(() => {
      appState.currentIndex++;
      if (appState.currentIndex < appState.questions.length) {
        this.renderQuestion();
      } else {
        this.renderResults();
      }
    }, 1000);
  },

  renderResults() {
    appState.isFinished = true;
    const resultsPanel = createResultsPanel(
      appState.score,
      appState.questions.length,
      appState.categoryStats
    );
    this.container.innerHTML = resultsPanel;
  },

  restartTest() {
    appState.questions = this.shuffleArray([...questions]);
    this.renderWelcomeScreen();
  }
};

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { appState, App };
}