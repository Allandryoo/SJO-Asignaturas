const cambiar = document.querySelector("#cambiar");
const reset = document.querySelector("#reset");
const parrafo = document.querySelector("#parrafo-principal");

let textoOriginal = parrafo.textContent;

cambiar.addEventListener("click", () => { 
    parrafo.textContent = "El texto ha cambiado";
    parrafo.classList.add("estilo");
});

reset.addEventListener ("click", () =>{
    parrafo.textContent = textoOriginal;
    parrafo.classList.remove("estilo");
});