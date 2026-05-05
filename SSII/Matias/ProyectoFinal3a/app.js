/**
 * app.js — Lógica Principal y Orquestación
 * 
 * REGLAS (ver systemPatterns.md):
 * - Gestiona el estado centralizado de la aplicación.
 * - Maneja todos los eventos mediante event delegation.
 * - Llama a las funciones de components.js para renderizar la UI.
 * - Único archivo que modifica el DOM.
 */

// ==================== ESTADO ====================
const state = {
    screen: 'welcome',       // 'welcome' | 'quiz' | 'results'
    category: null,           // categoría seleccionada
    questions: [],            // preguntas del test actual (barajadas)
    currentQuestion: 0,       // índice de la pregunta actual
    score: 0,                 // número de aciertos
    answers: [],              // historial de respuestas
    selectedOption: null,     // opción seleccionada actualmente
    showFeedback: false       // mostrar feedback de respuesta
};

// ==================== UTILIDADES ====================

/**
 * Baraja un array usando el algoritmo Fisher-Yates.
 * @param {Array} array - Array a barajar
 * @returns {Array} Nuevo array barajado
 */
function shuffleArray(array) {
    const shuffled = [...array];
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    return shuffled;
}

/**
 * Obtiene el nombre de una categoría por su ID.
 * @param {string} categoryId 
 * @returns {string}
 */
function getCategoryName(categoryId) {
    const cat = CATEGORIES.find(c => c.id === categoryId);
    return cat ? cat.name : categoryId;
}

// ==================== RENDERIZADO ====================

/**
 * Renderiza la UI según el estado actual.
 * Lee el estado y llama a los componentes apropiados.
 */
function render() {
    const app = document.getElementById('app');
    let html = createHeader('Autoescuela de Sistemas');

    switch (state.screen) {
        case 'welcome':
            html += createWelcomeScreen(CATEGORIES);
            break;

        case 'quiz':
            const question = state.questions[state.currentQuestion];
            html += createQuestionCard(
                question,
                state.currentQuestion,
                state.questions.length,
                state.selectedOption,
                state.showFeedback
            );
            break;

        case 'results':
            html += createResultsPanel(
                state.score,
                state.questions.length,
                state.answers,
                getCategoryName(state.category)
            );
            break;
    }

    app.innerHTML = html;
}

// ==================== ACCIONES ====================

/**
 * Selecciona una categoría e inicia el test.
 * @param {string} categoryId - ID de la categoría
 */
function selectCategory(categoryId) {
    const categoryQuestions = QUESTIONS.filter(q => q.category === categoryId);
    const shuffled = shuffleArray(categoryQuestions);

    state.screen = 'quiz';
    state.category = categoryId;
    state.questions = shuffled;
    state.currentQuestion = 0;
    state.score = 0;
    state.answers = [];
    state.selectedOption = null;
    state.showFeedback = false;

    render();
}

/**
 * Selecciona una opción de respuesta.
 * @param {number} optionIndex - Índice de la opción seleccionada
 */
function selectOption(optionIndex) {
    if (state.showFeedback) return; // Ya se ha respondido

    const question = state.questions[state.currentQuestion];
    const isCorrect = optionIndex === question.correct;

    state.selectedOption = optionIndex;
    state.showFeedback = true;

    if (isCorrect) {
        state.score++;
    }

    // Guardar respuesta en el historial
    state.answers.push({
        question: question.question,
        selected: question.options[optionIndex],
        correct: question.options[question.correct],
        isCorrect: isCorrect
    });

    render();
}

/**
 * Avanza a la siguiente pregunta o muestra resultados.
 */
function nextQuestion() {
    if (state.currentQuestion < state.questions.length - 1) {
        state.currentQuestion++;
        state.selectedOption = null;
        state.showFeedback = false;
        render();
    } else {
        // Última pregunta → mostrar resultados
        state.screen = 'results';
        render();
    }
}

/**
 * Reintenta el test con la misma categoría.
 */
function retryTest() {
    selectCategory(state.category);
}

/**
 * Vuelve a la pantalla de bienvenida.
 */
function goHome() {
    state.screen = 'welcome';
    state.category = null;
    state.questions = [];
    state.currentQuestion = 0;
    state.score = 0;
    state.answers = [];
    state.selectedOption = null;
    state.showFeedback = false;

    render();
}

// ==================== EVENT DELEGATION ====================

/**
 * Manejador principal de clicks.
 * Usa data-action para determinar la acción a ejecutar.
 * @param {Event} event
 */
function handleClick(event) {
    const target = event.target.closest('[data-action]');
    if (!target) return;

    const action = target.dataset.action;

    switch (action) {
        case 'select-category':
            selectCategory(target.dataset.category);
            break;
        case 'select-option':
            selectOption(parseInt(target.dataset.option));
            break;
        case 'next-question':
            nextQuestion();
            break;
        case 'retry':
            retryTest();
            break;
        case 'go-home':
            goHome();
            break;
    }
}

// ==================== INICIALIZACIÓN ====================

document.addEventListener('DOMContentLoaded', () => {
    const app = document.getElementById('app');
    app.addEventListener('click', handleClick);
    render();
});
