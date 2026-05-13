const navBar = document.querySelectorAll(".header-top nav a");
const textoNav = document.querySelector(".nav-contexto");

const btnInicio = document.querySelector("#btn-acceso");
const overlay = document.querySelector("#modal-overlay");
const btnCerrar = document.querySelector("#cerrar-modal");

const inputEmail = document.querySelector("#modal-email");
const inputPassword = document.querySelector("#modal-pass");

const errorEmail = document.querySelector(".msg-error-email");
const errorPass = document.querySelector(".msg-error-password");
const errorGeneral = document.querySelector("#modal-error-general");

const form = document.querySelector("#form-login");
let regexEmail = /^[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}$/;

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    errorEmail.textContent = "";
    errorPass.textContent = "";
    errorGeneral.textContent = "";

    const email = inputEmail.value.trim();
    const pass = inputPassword.value;

    let hayError = false;

    if (email.value == "") {
        errorEmail.textContent = "El email no puede estar vacio";
        hayError = true;
    } else if (!regexEmail.test(email.value)) {
        errorEmail.textContent = 'Formato del correo incorrecto';
        hayError = true;
    }

    if (pass == "") {
        errorPass.textContent = "La contraseña no puede estar vacia";
        hayError = true;
    };

    if (hayError) {
        return;
    }

    const loginCorrecto = await iniciarSesion(email, pass)

    if (loginCorrecto) {
        overlay.classList.add("oculto")
    } else {
        errorGeneral.textContent = "Correo o contraseña incorrectos"
    }

});

async function iniciarSesion(email, pass) {
    const response = await fetch("data/usuarios.json");
    const users = await response.json();

    const usuario = users.usuarios.find(
        (user) => user.email === email && user.password === pass
    );

    return usuario !== undefined;
}

btnInicio.addEventListener("click", () => {
    overlay.classList.remove("oculto")
});
btnCerrar.addEventListener("click", () => {
    overlay.classList.add("oculto")
});


navBar.forEach(link => {
    link.addEventListener("click", () => {
        navBar.forEach(des => des.classList.remove("subrayado"));
        link.classList.add("subrayado");
        textoNav.innerHTML = "Has hecho click en " + link.textContent;
    });
});

async function cargarCatalogo() {
    const response = await fetch('data/catalogo.json');
    const productos = await response.json();
    console.log(productos);

    const listaProductos = document.querySelector("#lista-productos");

    let tarjeta = "";
    productos.productos.forEach(producto => {
        tarjeta += `
        <div class="card">
            <img src="${producto.imagen}" alt="">
            <div class="card-body">
                <h3>${producto.nombre}</h3>
                <p class="precio">${producto.precio}€</p>
                <p class="extra">${producto.categoria}</p>
            </div>
        </div>
        `
    });
    listaProductos.innerHTML = tarjeta;
}
cargarCatalogo();
