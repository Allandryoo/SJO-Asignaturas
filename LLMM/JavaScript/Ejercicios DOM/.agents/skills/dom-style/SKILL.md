---
name: dom-style
description: Guía al agente para estilizar y programar ejercicios de manipulación del DOM con HTML, CSS moderno y JavaScript limpio.
---
# Estilo y Desarrollo DOM Premium

Esta skill define el estándar de calidad para todos los ejercicios de manipulación del DOM en este espacio de trabajo. Se activa automáticamente cuando se crean o modifican interfaces interactivas y scripts en JavaScript.

## Guías de CSS y Estética Visual

Para lograr interfaces premium y modernas (Glassmorphism, Modo Oscuro, etc.), aplica siempre las siguientes reglas:
1. **Paleta de Colores Curada:** Evita colores básicos (como `red`, `blue`, `green`). Utiliza colores basados en HSL o variables CSS con una estética moderna.
2. **Tipografía:** Importa y utiliza fuentes modernas (como Inter, Roboto o Outfit) a través de Google Fonts en lugar de las tipografías por defecto del navegador.
3. **Gradientes y Bordes:** Usa bordes redondeados (`border-radius: 12px` o superior) y gradientes suaves para fondos y botones.
4. **Interactividad y Micro-animaciones:** Agrega transiciones (`transition: all 0.3s ease`) y efectos hover en los botones y tarjetas para que la interfaz se sienta responsiva y viva.
5. **Sin Placeholders:** Evita textos o imágenes de relleno genéricos. Diseña con contenido real y estructurado.

## Estándares de JavaScript para DOM

1. **Uso de API Moderna:** Usa `querySelector` y `querySelectorAll` en lugar de `getElementById`.
2. **Código Limpio:** Declara variables con `const` y `let` (nunca uses `var`).
3. **Delegación de Eventos:** Si se añaden eventos a múltiples elementos similares, usa delegación de eventos en un contenedor común.
4. **Semántica HTML:** Asegúrate de que las interacciones usen elementos semánticos (por ejemplo, botones `<button>` con `id` descriptivos e interactividad por teclado).

## Estructura de Proyecto Recomendada
Cada ejercicio debe componerse de:
- `index.html` (Estructura semántica y metatags)
- `style.css` (Estilos responsivos y premium)
- `script.js` (Lógica limpia e interactividad)
