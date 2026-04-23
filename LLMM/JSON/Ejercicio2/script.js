let alumnos = [];

async function cargarAlumnos() {
    const response = await fetch("alumnos.json")
    const datos = await response.json();

    const contenedorAlumnos = document.querySelector("#tabla-alumnos")
}

datos.alumnos.array.forEach(alumno => {
    alumnos +=
    
});

function mostrarAlumnos(lista) {

}

document.getElementById("btnTodos").addEventListener("click", () => {

});

document.getElementById("btnAprobados").addEventListener("click", () => {

});

cargarAlumnos();