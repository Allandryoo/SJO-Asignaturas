# System Patterns - Reglas Técnicas

## Arquitectura del Proyecto

La aplicación sigue una arquitectura de separación de responsabilidades:
- **components.js**: Solo contiene funciones puras que reciben datos y devuelven strings HTML
- **app.js**: Maneja la lógica de la aplicación, estado centralizado y eventos
- **questions.js**: Solo contiene los datos (array de preguntas), sin lógica

## Principios de Diseño

### Componentes Puros (components.js)
- Cada función recibe datos como parámetros
- Devuelve exclusivamente strings de HTML
- No tiene副作用 (no modifica estado, no accede a DOM directamente)
- Nombre de función descriptivo: `createWelcomeScreen()`, `createQuestionCard()`, `createResultsPanel()`

### Lógica de Aplicación (app.js)
- Estado centralizado en un objeto
- Manejo de eventos usando event delegation sobre un contenedor principal
- Orquesta la aplicación llamando a funciones de components.js
- Actualiza el DOM manipulando el contenedor principal

### Datos (questions.js)
- Array de objetos con estructura: `{ id, category, question, options, correctAnswer }`
- Solo exporta los datos, sin funciones ni lógica
-Organizado en 5 categorías

## Estructura de Archivos

```
/proyecto
  /memory-bank
    productContext.md
    systemPatterns.md
    activeContext.md
    progress.md
  index.html
  style.css
  components.js
  app.js
  questions.js
```

## Convenciones de Código

- Funciones en inglés con camelCase
- Variables en inglés
- Comentarios en español cuando sea necesario
- Código limpio y legible