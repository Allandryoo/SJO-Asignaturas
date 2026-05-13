import { students } from "../datos/estudiantes.mjs";
export function renderStudentCards() {
    const section1 = document.getElementById("section1");
    section1.innerHTML = "";
    students.forEach(student => {
        const studentCard = document.createElement("div");
        studentCard.className = "student-card";
        studentCard.innerHTML = `
<h3>${student.nombre} ${student.apellido}</h3>
<p>Altura: ${student.altura}</p>
<p>Edad: ${student.edad}</p>
<p>Teléfono: ${student.telefono}</p>
`;
        section1.appendChild(studentCard);
    });
}
export function fichaStyles() {
    return `
.student-card {
border: 1px solid #ccc;
padding: 10px;
margin: 10px;
border-radius: 5px;
background-color: #f9f9f9;
}
.student-card h3 { margin-top: 0; }
.student-card p { margin: 5px 0; }
`;
}