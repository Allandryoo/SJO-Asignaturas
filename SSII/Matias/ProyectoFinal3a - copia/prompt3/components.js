function createWelcomeScreen(title, subtitle) {
  return `
    <div class="welcome-screen">
      <h1 class="title">${title}</h1>
      <p class="subtitle">${subtitle}</p>
      <button id="start-btn" class="btn-primary">Comenzar Test</button>
    </div>
  `;
}

function createQuestionCard(questionData) {
  const optionsHTML = questionData.options.map((option, index) => `
    <button class="option-btn" data-option="${option}">${option}</button>
  `).join('');

  return `
    <div class="question-card">
      <div class="question-header">
        <span class="category-badge">${questionData.category}</span>
        <span class="question-number">Pregunta ${questionData.id}</span>
      </div>
      <h2 class="question-text">${questionData.question}</h2>
      <div class="options-container">
        ${optionsHTML}
      </div>
    </div>
  `;
}

function createResultsPanel(score, total, categoryStats) {
  const percentage = Math.round((score / total) * 100);
  const passed = percentage >= 60;

  const categoriesHTML = Object.entries(categoryStats).map(([cat, stats]) => `
    <div class="category-stat">
      <span class="cat-name">${cat}</span>
      <span class="cat-score">${stats.correct}/${stats.total}</span>
    </div>
  `).join('');

  return `
    <div class="results-panel">
      <h2 class="results-title">${passed ? '¡Felicidades!' : 'Sigue Practicando'}</h2>
      <div class="score-display">
        <span class="score-number">${score}</span>
        <span class="score-separator">/</span>
        <span class="score-total">${total}</span>
      </div>
      <p class="percentage">${percentage}% de aciertos</p>
      <div class="category-stats">
        ${categoriesHTML}
      </div>
      <button id="restart-btn" class="btn-primary">Reiniciar Test</button>
    </div>
  `;
}

function createProgressBar(current, total) {
  const percentage = (current / total) * 100;
  return `
    <div class="progress-container">
      <div class="progress-bar">
        <div class="progress-fill" style="width: ${percentage}%"></div>
      </div>
      <span class="progress-text">${current} / ${total}</span>
    </div>
  `;
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { createWelcomeScreen, createQuestionCard, createResultsPanel, createProgressBar };
}