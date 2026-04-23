async function cargarVideojuegos() {
    const response = await fetch("videojuegos.json")
    const juegos = await response.json()
    const contenedor = document.querySelector("#contenedor")

    let allGames = "";
    juegos.videojuegos.forEach(juego => {
        allGames += `
        <div class="tarjeta">
            <img src="${juego.imagen}"></img>
            <h3>${juego.titulo}</h3>
            <p>Género: ${juego.genero}</p>
            <p>Precio: ${juego.precio}€</p>
            <p>Multijugador: ${juego.multijugador ? "Si" : "No"}</p>
            <p>Individual: ${juego.individual ? "Si" : "No"}</p>
        </div>
        `
    })
    contenedor.innerHTML = allGames;
}

cargarVideojuegos();