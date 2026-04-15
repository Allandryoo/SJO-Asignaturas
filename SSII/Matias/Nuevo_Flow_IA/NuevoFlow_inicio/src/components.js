/**
 * components.js — Vista (MVC)
 *
 * Reglas aplicadas (.antigravity/rules.md):
 *   • Cada función es pura: recibe datos solo por parámetros.
 *   • No accede a variables externas ni modifica estado global.
 *   • Devuelve un String de HTML listo para renderizar.
 */

/**
 * Crea la barra de navegación.
 * @param {string} title - Título a mostrar en el navbar.
 * @returns {string} HTML del componente <nav>.
 */
function createNavbar(title) {
  return `<nav><h1>${title}</h1></nav>`;
}

/**
 * Crea el bloque de contenido principal.
 * @param {string} text - Texto a mostrar dentro del contenido.
 * @returns {string} HTML del componente <div>.
 */
function createContent(text) {
  return `<div class="content"><p>${text}</p></div>`;
}
