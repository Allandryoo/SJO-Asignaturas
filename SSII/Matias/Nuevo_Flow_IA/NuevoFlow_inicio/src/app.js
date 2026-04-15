/**
 * app.js — Controlador (MVC)
 *
 * Reglas aplicadas (.antigravity/rules.md):
 *   • Toda la lógica está dentro de funciones.
 *   • main() actúa como despachador/orquestador del renderizado.
 *   • No hay estado global; los datos se pasan por parámetros.
 *   • Depende de los componentes puros definidos en components.js.
 */

/**
 * Renderiza el HTML generado dentro del contenedor raíz.
 * @param {string} containerId - ID del elemento DOM donde se inyecta la UI.
 * @param {string} html       - String de HTML a insertar.
 */
function render(containerId, html) {
  document.getElementById(containerId).innerHTML = html;
}

/**
 * Punto de entrada de la aplicación.
 * Orquesta el renderizado componiendo las funciones de la Vista.
 */
function main() {
  const title   = "Mi SPA Minimalista";
  const content = "Bienvenido. Este contenido fue generado dinámicamente.";

  const view =
    createNavbar(title) +
    createContent(content);

  render("app", view);
}

// Arranca la aplicación cuando el DOM esté listo
document.addEventListener("DOMContentLoaded", main);
