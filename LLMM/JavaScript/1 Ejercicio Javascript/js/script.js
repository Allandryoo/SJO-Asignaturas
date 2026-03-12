const linkCabeceras = document.querySelectorAll(".navbar a");
const titulo = document.querySelector(".topbar span");
const contenidoTitulo = titulo.textContent;

linkCabeceras.forEach(link => {
    link.addEventListener("click", () => {
        linkCabeceras.forEach(l => l.classList.remove("active"));
        link.classList.add("active");
        titulo.textContent = contenidoTitulo + " estas en " + link.textContent;
    });
});

const tarjetaProducto = document.querySelectorAll(".products .card");
let imagenFondo = document.querySelector(".inicio img");
const imagenPredeterminada = document.querySelector(".topbar")

imagenPredeterminada.addEventListener("click", () => {
    imagenFondo.src="img/fondo.png"
})
tarjetaProducto[0].addEventListener("click", () => {
    imagenFondo.src = "img/ratong.png"
    imagenFondo.style.width = "100%"
    imagenFondo.style.height = "300px"
});
tarjetaProducto[1].addEventListener("click", () => {
    imagenFondo.src = "img/monitorg.png"
    imagenFondo.style.width = "100%"
    imagenFondo.style.height = "300px"
});
tarjetaProducto[2].addEventListener("click", () => {
    imagenFondo.src = "img/hddg.png"
    imagenFondo.style.width = "100%"
    imagenFondo.style.height = "300px"
});
tarjetaProducto[3].addEventListener("click", () => {
    imagenFondo.src = "img/portatilg.png"
    imagenFondo.style.width = "100%"
    imagenFondo.style.height = "300px"
});