const boton = document.querySelector("button");
const lista = document.querySelector("ul");

boton.addEventListener("click", () => { 
    
    let numeroNuevo = document.createElement("li");
    
    numeroNuevo.textContent = Math.floor(Math.random() * 100);

    lista.appendChild(numeroNuevo);
});