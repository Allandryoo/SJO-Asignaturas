const formulario = document.querySelector("#formulario");
const parrafo = document.querySelector("#parrafo");
const añadirBtn = document.querySelector("#añadir");

añadirBtn.addEventListener("click", (e) => {
    e.preventDefault(); 
    
    let parrafoNuevo = document.createElement("div");
    parrafoNuevo.classList.add("mensaje");
    
    parrafoNuevo.textContent = parrafo.value; 

    formulario.before(parrafoNuevo);
    parrafo.value = "";
});