let alumnos = [];
const contenedorAlumnos = document.getElementById("tabla-alumnos")

async function cargarAlumnos() {
    const response = await fetch("alumnos.json")
    const datos = await response.json();
    console.log(datos)
    datos.alumnos.forEach(alumno => {
        alumnos +=
            `
            <tr>    
                <td>${alumno.nombre}</td>
                <td>${alumno.edad}</td>
                <td>${alumno.curso}</td>
                <td>${alumno.notaMedia}</td>
            </tr>
            `
    });
    contenedorAlumnos.innerHTML = alumnos;
}

function mostrarAlumnos(lista) {

}

document.getElementById("btnTodos").addEventListener("click", () => {
    cargarAlumnos()
});

document.getElementById("btnAprobados").addEventListener("click", () => {

});

cargarAlumnos();