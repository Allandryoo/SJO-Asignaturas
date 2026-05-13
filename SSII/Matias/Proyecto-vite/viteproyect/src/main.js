import { Navbar } from './componentes/navbar.mjs';
import { renderStudentCards, fichaStyles } from './componentes/fichas_estudiantes.mjs';
const app = document.body;
// Añadimos componentes
app.append(Navbar());
renderStudentCards();

// Insertar estilos de fichas
const styleFicha = document.createElement("style");
styleFicha.textContent = fichaStyles();
document.head.appendChild(styleFicha);