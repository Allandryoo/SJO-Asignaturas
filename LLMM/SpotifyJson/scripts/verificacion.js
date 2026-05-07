const btnIniciarSesion = document.querySelector("#BtnIniciarSesion");
const formulario = document.querySelector("#formulario");
const btnCrearLista = document.querySelector(".sec-izq-caja button");
let regexEmail = /^[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}$/;

let sesionIniciada = false;

async function mostrarFormulario() {
    if (sesionIniciada) {
        sesionIniciada = false;
        btnIniciarSesion.textContent = "Iniciar sesión";
        return;
    }
    const response = await fetch("../datos/data.json");
    const data = await response.json();

    const IniciarSesion = data.form[0].nombre;
    const textoEmail = data.form[0].correo;
    const textoPassword = data.form[0].contraseña;
    const textoBoton = data.form[0].botonContinuar;

    formulario.innerHTML = `
        <div id="overlay"></div>
        <form>
            <img src="../img/logo2.svg" alt="Spotify" class="logo-form">
            <h2>${IniciarSesion}</h2>

            <label for="email">${textoEmail}</label>
            <input type="text" id="email" name="email" placeholder="nombre@ejemplo.com">
            <span id="errorEmail"></span>

            <label for="password">${textoPassword}</label>
            <input type="password" id="password" name="password" placeholder="Contraseña">
            <span id="errorPassword"></span>

            <span id="errorGeneral"></span>

            <button type="submit">${textoBoton}</button>
            <button type="button" id="btnCerrar">Cancelar</button>
        </form>
    `;

    document.querySelector("#btnCerrar").addEventListener("click", () => {
        formulario.innerHTML = "";
    });

    document.querySelector("#overlay").addEventListener("click", () => {
        formulario.innerHTML = "";
    });
    document.querySelector("form").addEventListener("submit", async (event) => {
        event.preventDefault();

        const emailInput = document.querySelector("#email");
        const passwordInput = document.querySelector("#password");
        const errorEmail = document.querySelector("#errorEmail");
        const errorPassword = document.querySelector("#errorPassword");
        const errorGeneral = document.querySelector("#errorGeneral");

        const email = emailInput.value.trim();
        const password = passwordInput.value;

        errorEmail.textContent = "";
        errorPassword.textContent = "";
        errorGeneral.textContent = "";

        let hayError = false;

        if (email === "") {
            errorEmail.textContent = "El correo electrónico no puede estar vacío";
            hayError = true;
        } else if (!regexEmail.test(email)) {
            errorEmail.textContent = 'El correo debe tener un formato válido (ej: nombre@ejemplo.com)';
            hayError = true;
        }

        if (password === "") {
            errorPassword.textContent = "La contraseña no puede estar vacía";
            hayError = true;
        }

        if (hayError) {
            return;
        }

        const loginCorrecto = await iniciarSesion(email, password);

        if (loginCorrecto) {
            formulario.innerHTML = "";
            sesionIniciada = true;
            btnIniciarSesion.textContent = "Cerrar sesión";
        } else {
            errorGeneral.textContent = "Correo electrónico o contraseña incorrectos";
        }
    });
}


btnIniciarSesion.addEventListener("click", () => {
    mostrarFormulario();
});


btnCrearLista.addEventListener("click", () => {
    mostrarFormulario();
});
document.addEventListener("click", (event) => {
    if (event.target.closest(".tarjeta")) {
        mostrarFormulario();
    }
});

async function iniciarSesion(email, password) {
    const response = await fetch("../datos/users.json");
    const data = await response.json();

    const usuario = data.users.find(
        (user) => user.correo === email && user.contraseña === password
    );

    return usuario !== undefined;
}