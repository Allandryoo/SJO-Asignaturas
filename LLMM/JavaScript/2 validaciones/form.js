let inputEmail1 = document.querySelector("#email1");
let inputEmail2 = document.querySelector("#email2");
let inputPass1 = document.querySelector("#pass1");
let inputPass2 = document.querySelector("#pass2");
let inputEdad = document.querySelector("#edad");
let inputTelefono = document.querySelector("#telefono");
let inputDni = document.querySelector("#dni");
let errorMail = document.querySelector("#errorMail");
let errorPass = document.querySelector("#errorPass");

let regexEmail = /^[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}$/;
let regexPass = /^[a-zA-Z0-9._%+-]{6,}$/;
let regexDni = /^\d{8}[A-HJ-NP-TV-Z]$/;

function comprobar_email(email,) {
    let valor = email.value
    if(!regexEmail.test(valor)){
        email.classList.remove("ok");
        email.classList.add("error")
    }else {
        email.classList.remove("error");
        email.classList.add("ok")
    }
}

function comprobar_pass(pass) {
    let valor = pass.value
    if(!regexPass.test(valor)){
        pass.classList.remove("ok");
        pass.classList.add("error")
    }else {
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