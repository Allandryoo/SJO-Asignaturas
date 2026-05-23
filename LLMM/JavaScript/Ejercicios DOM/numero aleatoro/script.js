const boton = document.querySelector("#btn-generar");
const lista = document.querySelector("#lista-numeros");

boton.addEventListener("click", () => { 
    const numeroNuevo = document.createElement("li");
    numeroNuevo.textContent = Math.floor(Math.random() * 100);
    numeroNuevo.classList.add("number-item");
    lista.appendChild(numeroNuevo);
});