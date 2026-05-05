async function cargarCanciones() {
    const response = await fetch("../datos/data.json");
    const canciones = await response.json();


    const contenedor = document.querySelector("#canciones");

    let tarjeta = "";
    canciones.canciones.forEach(cancion => {
        tarjeta += `
            <div class="tarjeta">
                <img src="${cancion.imagen}" alt="${cancion.titulo}">
                <h3>${cancion.titulo}</h3>
                <p><span class="mini">E</span>${cancion.artista}</p>
            </div>
            `
    });
    contenedor.innerHTML = tarjeta;
}


async function cargarArtistas() {
    const response = await fetch("../datos/data.json");
    const artistas = await response.json();
    console.log(artistas)

    const contenedor = document.querySelector("#artistas");

    let tarjeta = "";
    artistas.artistas.forEach(artista => {
        console.log(artista.nombre)
        tarjeta += `
            <div class="tarjeta">
                <img class="artista" src="${artista.imagen}" alt="${artista.nombre}">
                <h3>${artista.nombre}</h3>
                <p>Artista</p>
            </div>
            `
    });
    contenedor.innerHTML = tarjeta;
}

async function cargarAlbumes() {
    const response = await fetch("../datos/data.json");
    const albumes = await response.json();

    const contenedor = document.querySelector("#albumes");

    let tarjeta = "";
    albumes.albumes.forEach(album => {
        tarjeta += `
            <div class="tarjeta">
                <img src="${album.imagen}" alt="${album.nombre}">
                <h3>${album.titulo}</h3>
                <p>${album.artista}</p>
            </div>
            `
    });
    contenedor.innerHTML = tarjeta;
}

async function cargarEmisoras() {
    const response = await fetch("../datos/data.json")
    const emisoras = await response.json();

    const contenedor = document.querySelector("#emisoras");

    let tarjeta = ""
    emisoras.emisoras.forEach(emisora => {
        tarjeta += `
        <div class="tarjeta">
            <img src="${emisora.imagen}" alt="${emisora.nombre}">
            <p>${emisora.nombre}</p>
        </div>
        `
    });
    contenedor.innerHTML = tarjeta;
}

async function cargarListas() {
    const response = await fetch("../datos/data.json")
    const listas = await response.json();

    const contenedor = document.querySelector("#listas");

    let tarjeta = ""
    listas.listas.forEach(lista => {
        tarjeta += `
        <div class="tarjeta">
            <img src="${lista.imagen}" alt="${lista.nombre}">
            <p>${lista.nombre}</p>
        </div>
        `
    });
    contenedor.innerHTML = tarjeta;
}


cargarCanciones();
cargarArtistas();
cargarAlbumes();
cargarEmisoras();
cargarListas();
