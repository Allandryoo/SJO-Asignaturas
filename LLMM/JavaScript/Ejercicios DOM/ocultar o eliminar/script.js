const p = document.querySelectorAll("p");
const boton = document.querySelector("button");

p.forEach(p => {
    p.addEventListener("click", () => { 
        p.style.display = "none";
    });
});
p.forEach(p => {
    p.addEventListener("dblclick", () => { 
        p.remove();
    });
});
boton.addEventListener("click", () => { 
    p.forEach(p => { 
        p.style.display = "block";
    });
});

