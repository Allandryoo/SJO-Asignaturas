const contenedor = document.querySelector("#contenedor");
let peliculas = [];

async function cargarPeliculas() {
    const respuesta = await fetch("peliculas.json");
    const datos = await respuesta.json();
    peliculas = datos.peliculas;
    pintarPeliculas(peliculas);
}

function pintarPeliculas(lista) {
    contenedor.innerHTML = "";

    if (lista.length === 0) {
        contenedor.innerHTML = "<p>No se encuentran pelis</p>";
        return;
    }

    lista.forEach(pelicula => {
        contenedor.innerHTML += `
        <div class="tarjeta">
            <h2>${pelicula.titulo}</h2>
            <p>${pelicula.director}</p>
            <p>${pelicula.anio}</p>
            <p>${pelicula.genero}</p>
        </div>
        `;
    });
}

document.getElementById("buscador").addEventListener("input", (event) => {
    let busca = event.target.value.toLowerCase();
    let pelisFiltradas = peliculas.filter(pelicula => pelicula.titulo.toLowerCase().includes(busca));
    pintarPeliculas(pelisFiltradas);

});

cargarPeliculas();