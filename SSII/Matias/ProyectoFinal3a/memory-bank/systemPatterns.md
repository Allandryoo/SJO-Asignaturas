# System Patterns — Autoescuela de Sistemas

## Arquitectura General
Aplicación **SPA** (Single Page Application) vanilla, sin frameworks. Toda la UI se renderiza dentro de un contenedor `<div id="app">`.

## Reglas Técnicas Obligatorias

### 1. Separación de Responsabilidades

| Archivo | Responsabilidad | Regla |
|---|---|---|
| `components.js` | **Vista** — Funciones puras que devuelven HTML | NO puede acceder a estado global, NO puede añadir event listeners, NO puede modificar el DOM |
| `app.js` | **Lógica** — Estado, eventos, navegación, orquestación | Único archivo que gestiona el estado y llama a `render()` |
| `questions.js` | **Datos** — Banco de preguntas | Solo exporta datos, no contiene lógica |

### 2. Funciones Puras en `components.js`
```
function createComponent(data) → string HTML
```
- Reciben datos como parámetros
- Devuelven un string HTML
- Sin efectos secundarios
- Sin acceso a variables globales
- Sin manipulación directa del DOM

### 3. Estado Centralizado en `app.js`
```js
const state = {
    screen: 'welcome',      // 'welcome' | 'quiz' | 'results'
    category: null,          // categoría seleccionada
    questions: [],           // preguntas del test actual
    currentQuestion: 0,      // índice de la pregunta actual
    score: 0,                // aciertos
    answers: [],             // historial de respuestas
    selectedOption: null,    // opción seleccionada (para feedback)
    showFeedback: false      // mostrar feedback antes de avanzar
};
```

### 4. Patrón de Renderizado
```
Estado cambia → render() → lee state → llama a componentes → innerHTML en #app
```

### 5. Event Delegation
Todos los eventos se gestionan mediante un único listener en `#app` usando `data-action` attributes:
```js
document.getElementById('app').addEventListener('click', handleClick);
```

### 6. Flujo de Pantallas
```
[Welcome] → seleccionar categoría → [Quiz] → responder todas → [Results] → reintentar → [Welcome]
```

## Convenciones de Código
- **Nombres de funciones de componentes**: `create` + NombreComponente (ej: `createHeader`)
- **Nombres de acciones**: `data-action="nombre"` en elementos HTML interactivos
- **IDs únicos**: todos los elementos interactivos tienen IDs descriptivos
- **Sin dependencias externas**: solo vanilla HTML/CSS/JS + Google Fonts
