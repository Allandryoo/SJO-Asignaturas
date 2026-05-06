/**
 * components.js — Componentes de UI (Funciones Puras)
 * 
 * REGLAS (ver systemPatterns.md):
 * - Cada función recibe datos como parámetros y devuelve un string HTML.
 * - NO accede a estado global.
 * - NO añade event listeners.
 * - NO modifica el DOM directamente.
 */

/**
 * Crea la cabecera de la aplicación.
 * @param {string} title - Título a mostrar
 * @returns {string} HTML string
 */
function createHeader(title) {
    return `
        <header class="header">
            <div class="header__logo">
                <span class="header__icon">🚗</span>
                <h1 class="header__title">${title}</h1>
            </div>
            <p class="header__subtitle">Prepárate para dominar los sistemas informáticos</p>
        </header>
    `;
}

/**
 * Crea la pantalla de bienvenida con selector de categorías.
 * @param {Array} categories - Lista de categorías disponibles
 * @returns {string} HTML string
 */
function createWelcomeScreen(categories) {
    const categoryCards = categories.map(cat => `
        <button class="category-card" data-action="select-category" data-category="${cat.id}" id="category-${cat.id}">
            <span class="category-card__icon">${cat.icon}</span>
            <h3 class="category-card__name">${cat.name}</h3>
            <p class="category-card__desc">${cat.description}</p>
        </button>
    `).join('');

    return `
        <div class="welcome animate-fade-in">
            <div class="welcome__hero">
                <h2 class="welcome__title">¿Listo para el examen?</h2>
                <p class="welcome__text">Elige una categoría y pon a prueba tus conocimientos con 5 preguntas.</p>
            </div>
            <div class="category-grid">
                ${categoryCards}
            </div>
        </div>
    `;
}

/**
 * Crea la barra de progreso del test.
 * @param {number} current - Pregunta actual (0-indexed)
 * @param {number} total - Total de preguntas
 * @returns {string} HTML string
 */
function createProgressBar(current, total) {
    const percentage = ((current) / total) * 100;
    return `
        <div class="progress-bar">
            <div class="progress-bar__info">
                <span>Pregunta ${current + 1} de ${total}</span>
                <span>${Math.round(percentage)}%</span>
            </div>
            <div class="progress-bar__track">
                <div class="progress-bar__fill" style="width: ${percentage}%"></div>
            </div>
        </div>
    `;
}

/**
 * Crea la tarjeta de una pregunta con sus opciones.
 * @param {Object} question - Objeto pregunta
 * @param {number} currentIndex - Índice actual (0-indexed)
 * @param {number} totalQuestions - Total de preguntas
 * @param {number|null} selectedOption - Opción seleccionada (null si no se ha seleccionado)
 * @param {boolean} showFeedback - Si se debe mostrar el feedback
 * @returns {string} HTML string
 */
function createQuestionCard(question, currentIndex, totalQuestions, selectedOption, showFeedback) {
    const options = question.options.map((option, index) => {
        let optionClass = 'option-btn';
        let disabled = '';

        if (showFeedback) {
            disabled = 'disabled';
            if (index === question.correct) {
                optionClass += ' option-btn--correct';
            } else if (index === selectedOption && index !== question.correct) {
                optionClass += ' option-btn--incorrect';
            }
        } else if (index === selectedOption) {
            optionClass += ' option-btn--selected';
        }

        return `
            <button class="${optionClass}" 
                    data-action="select-option" 
                    data-option="${index}" 
                    id="option-${index}"
                    ${disabled}>
                <span class="option-btn__letter">${String.fromCharCode(65 + index)}</span>
                <span class="option-btn__text">${option}</span>
            </button>
        `;
    }).join('');

    const feedbackButton = showFeedback ? `
        <button class="next-btn" data-action="next-question" id="btn-next">
            ${currentIndex < totalQuestions - 1 ? 'Siguiente pregunta →' : 'Ver resultados 🏁'}
        </button>
    ` : '';

    return `
        <div class="quiz animate-fade-in">
            ${createProgressBar(currentIndex, totalQuestions)}
            <div class="question-card">
                <div class="question-card__category">
                    <span>${question.category.toUpperCase()}</span>
                </div>
                <h2 class="question-card__text">${question.question}</h2>
                <div class="options-grid">
                    ${options}
                </div>
                ${feedbackButton}
            </div>
        </div>
    `;
}

/**
 * Crea el panel de resultados del test.
 * @param {number} score - Número de aciertos
 * @param {number} totalQuestions - Total de preguntas
 * @param {Array} answers - Historial de respuestas [{question, selected, correct, isCorrect}]
 * @param {string} categoryName - Nombre de la categoría
 * @returns {string} HTML string
 */
function createResultsPanel(score, totalQuestions, answers, categoryName) {
    const percentage = Math.round((score / totalQuestions) * 100);
    
    let emoji, message, messageClass;
    if (percentage === 100) {
        emoji = '🏆';
        message = '¡Perfecto! ¡Dominas esta categoría!';
        messageClass = 'results__message--perfect';
    } else if (percentage >= 60) {
        emoji = '👏';
        message = '¡Buen trabajo! Vas por buen camino.';
        messageClass = 'results__message--good';
    } else {
        emoji = '💪';
        message = 'Sigue practicando, ¡tú puedes!';
        messageClass = 'results__message--retry';
    }

    const answersList = answers.map((ans, i) => `
        <div class="result-item ${ans.isCorrect ? 'result-item--correct' : 'result-item--incorrect'}">
            <div class="result-item__indicator">${ans.isCorrect ? '✅' : '❌'}</div>
            <div class="result-item__content">
                <p class="result-item__question">${i + 1}. ${ans.question}</p>
                <p class="result-item__answer">
                    Tu respuesta: <strong>${ans.selected}</strong>
                    ${!ans.isCorrect ? ` — Correcta: <strong>${ans.correct}</strong>` : ''}
                </p>
            </div>
        </div>
    `).join('');

    return `
        <div class="results animate-fade-in">
            <div class="results__hero">
                <span class="results__emoji">${emoji}</span>
                <h2 class="results__title">Resultados: ${categoryName}</h2>
                <p class="results__message ${messageClass}">${message}</p>
            </div>
            <div class="results__score-ring">
                <div class="score-circle">
                    <svg viewBox="0 0 120 120">
                        <circle class="score-circle__bg" cx="60" cy="60" r="52"></circle>
                        <circle class="score-circle__fill" cx="60" cy="60" r="52"
                                style="stroke-dasharray: ${percentage * 3.27}, 327"></circle>
                    </svg>
                    <div class="score-circle__text">
                        <span class="score-circle__number">${score}/${totalQuestions}</span>
                        <span class="score-circle__percent">${percentage}%</span>
                    </div>
                </div>
            </div>
            <div class="results__details">
                <h3>Resumen de respuestas</h3>
                ${answersList}
            </div>
            <div class="results__actions">
                <button class="btn btn--primary" data-action="retry" id="btn-retry">
                    🔄 Reintentar
                </button>
                <button class="btn btn--secondary" data-action="go-home" id="btn-home">
                    🏠 Elegir otra categoría
                </button>
            </div>
        </div>
    `;
}
