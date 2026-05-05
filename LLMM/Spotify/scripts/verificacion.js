const btnIniciarSesion = document.querySelector("#BtnIniciarSesion");
const formulario = document.querySelector("#formulario");
const btnCrearLista = document.querySelector(".sec-izq-caja button");

// Función para mostrar el formulario de login
function mostrarFormulario() {
    formulario.innerHTML = `
        <div id="overlay"></div>
        <form>
            <h2>Iniciar Sesión</h2>

            <label for="email">Correo electrónico</label>
            <input type="text" id="email" name="email" placeholder="nombre@ejemplo.com">
            <span id="errorEmail"></span>

            <label for="password">Contraseña</label>
            <input type="password" id="password" name="password" placeholder="Contraseña">
            <span id="error"></span>

            <button type="submit">Iniciar sesión</button>
            <button type="button" id="btnCerrar">Cancelar</button>
        </form>
    `;

    // Botón para cerrar el formulario
    document.querySelector("#btnCerrar").addEventListener("click", () => {
        formulario.innerHTML = "";
    });

    // Cerrar al hacer click en el overlay (fondo oscuro)
    document.querySelector("#overlay").addEventListener("click", () => {
        formulario.innerHTML = "";
    });
}

// Botón "Iniciar sesión" del header
btnIniciarSesion.addEventListener("click", () => {
    mostrarFormulario();
});

// Botón "Crear lista" de la sección izquierda
if (btnCrearLista) {
    btnCrearLista.addEventListener("click", () => {
        mostrarFormulario();
    });
}

// Click en cualquier tarjeta (.tarjeta) muestra el login
document.addEventListener("click", (event) => {
    if (event.target.closest(".tarjeta")) {
        mostrarFormulario();
    }
});

// Validar email: debe contener "@" y acabar en ".com"
function validarEmail(email) {
    return email.includes("@") && email.endsWith(".com");
}

// Envío del formulario (delegación de eventos porque el form se inyecta dinámicamente)
formulario.addEventListener("submit", async (event) => {
    event.preventDefault();

    const emailInput = document.querySelector("#email");
    const passwordInput = document.querySelector("#password");
    const errorEmail = document.querySelector("#errorEmail");
    const errorGeneral = document.querySelector("#error");

    const email = emailInput.value.trim();
    const password = passwordInput.value;

    // Limpiar errores previos
    errorEmail.textContent = "";
    errorGeneral.textContent = "";

    // Validar formato del email
    if (!validarEmail(email)) {
        errorEmail.textContent = 'El correo debe contener "@" y acabar en ".com"';
        return;
    }

    // Comprobar credenciales contra users.json
    const loginCorrecto = await iniciarSesion(email, password);

    if (loginCorrecto) {
        formulario.innerHTML = "";
        alert("¡Inicio de sesión correcto! Bienvenido.");
    } else {
        errorGeneral.textContent = "Correo electrónico o contraseña incorrectos";
    }
});

// Función async que comprueba las credenciales en users.json
async function iniciarSesion(email, password) {
    const response = await fetch("../datos/users.json");
    const data = await response.json();

    // Buscar un usuario cuyo correo Y contraseña coincidan
    const usuario = data.users.find(
        (user) => user.correo === email && user.contraseña === password
    );

    return usuario !== undefined;
}