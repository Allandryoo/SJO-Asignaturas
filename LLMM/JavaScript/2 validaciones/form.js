let inputEmail1 = document.querySelector("#email1");
let inputEmail2 = document.querySelector("#email2");
let inputPass1 = document.querySelector("#pass1");
let inputPass2 = document.querySelector("#pass2");
let inputEdad = document.getElementById("edad");
let inputTelefono = document.querySelector("#telefono");
let inputDni = document.querySelector("#dni");
let opciones = document.querySelectorAll("#opciones")
let condiciones = document.querySelector("#condiciones")

let errorMail = document.querySelector("#errorMail");
let errorPass = document.querySelector("#errorPass");


let regexEmail = /^[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}$/;
let regexPass = /^[a-zA-Z0-9._%+-]{6,}$/;
let regexDni = /^\d{8}[A-HJ-NP-TV-Z]$/;
let regexTlf = /^\d{9}$/;

function comprobar_email(email,) {
    let valor = email.value
    if (!regexEmail.test(valor)) {
        email.classList.remove("ok");
        email.classList.add("error")
    } else {
        email.classList.remove("error");
        email.classList.add("ok")
    }
}

function comprobar_pass(pass) {
    let valor = pass.value
    if (!regexPass.test(valor)) {
        pass.classList.remove("ok");
        pass.classList.add("error")
    } else {
        pass.classList.remove("error");
        pass.classList.add("ok")
    }
}

inputEmail1.addEventListener("input", () => {
    comprobar_email(inputEmail1)
})

inputEmail2.addEventListener("input", () => {
    comprobar_email(inputEmail2)
})

inputPass1.addEventListener("input", () => {
    comprobar_pass(inputPass1)
})

inputPass2.addEventListener("input", () => {
    comprobar_pass(inputPass2)
})

inputEmail2.addEventListener("input", () => {
    if (inputEmail1.value !== inputEmail2.value) {
        errorMail.textContent = "Los emails no coinciden"
    } else {
        errorMail.textContent = ""
    }
})

inputPass2.addEventListener("input", () => {
    if (inputPass1.value !== inputPass2.value) {
        errorPass.textContent = "Las contraseñas no coinciden"
    } else {
        errorPass.textContent = ""
    }
})

inputEdad.addEventListener("input", () => {
    let valor = inputEdad.value
    if (valor < 18) {
        inputEdad.classList.remove("ok");
        inputEdad.classList.add("error")
    } else {
        inputEdad.classList.remove("error");
        inputEdad.classList.add("ok")
    }
})

let formulario = document.querySelector("#formulario");
let selectOpciones = document.querySelector("#opciones");
let errorValidacionFinal = document.querySelector("#errorValidacionFinal");

function actualizarEstadoCampo(campo, esValido) {
    campo.classList.remove("error", "ok");
    campo.classList.add(esValido ? "ok" : "error");
}

function validarCoincidenciaEmail() {
    if (inputEmail2.value !== inputEmail1.value) {
        errorMail.textContent = "Los emails no coinciden";
    } else {
        errorMail.textContent = "";
    }
}

function validarCoincidenciaPass() {
    if (inputPass2.value !== inputPass1.value) {
        errorPass.textContent = "Las contraseñas no coinciden";
    } else {
        errorPass.textContent = "";
    }
}

inputEmail1.addEventListener("input", validarCoincidenciaEmail);
inputEmail2.addEventListener("input", validarCoincidenciaEmail);

inputPass1.addEventListener("input", validarCoincidenciaPass);
inputPass2.addEventListener("input", validarCoincidenciaPass);

formulario.addEventListener("submit", (evento) => {
    let errores = [];
    let emailValido = inputEmail1.value.includes("@");
    let passValida = inputPass1.value.length >= 6;
    let edadValida = Number(inputEdad.value) >= 18;
    let dniValido = regexDni.test(inputDni.value);
    let telefonoValido = inputTelefono.value.length === 9;
    let opcionValida = selectOpciones.value !== "";
    let condicionesValidas = condiciones.checked;

    if (!emailValido) {
        errores.push("El email debe contener una arroba.");
    }

    if (!passValida) {
        errores.push("La contraseña debe tener al menos seis caracteres.");
    }

    if (!edadValida) {
        errores.push("La edad debe ser mayor o igula a 18.");
    }

    if (!dniValido) {
        errores.push("El DNI no es válido.");
    }

    if (!telefonoValido) {
        errores.push("El teléfono debe tener exactamente 9 caracteres.");
    }

    if (!opcionValida) {
        errores.push("Debes escoger una opción del select.");
    }

    if (!condicionesValidas) {
        errores.push("Debes marcar el check de condiciones.");
    }

    actualizarEstadoCampo(inputEmail1, emailValido);
    actualizarEstadoCampo(inputEmail2, emailValido && inputEmail1.value === inputEmail2.value);
    actualizarEstadoCampo(inputPass1, passValida);
    actualizarEstadoCampo(inputPass2, passValida && inputPass1.value === inputPass2.value);
    actualizarEstadoCampo(inputEdad, edadValida);
    actualizarEstadoCampo(inputDni, dniValido);
    actualizarEstadoCampo(inputTelefono, telefonoValido);

    if (errores.length > 0) {
        evento.preventDefault();
        errorValidacionFinal.innerHTML = errores.join("<br>");
    } else {
        errorValidacionFinal.textContent = "";
    }
});

