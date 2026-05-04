const btnIniciarSesion = document.querySelector("#BtnIniciarSesion");
const formulario = document.querySelector("#formulario")

btnIniciarSesion.addEventListener("click", () => {
    formulario.innerHTML = `
        <form>
            <h2>Iniciar Sesión</h2>

            <label for="email">Correo electronico</label>
            <input type="text" id="email" name="email">

            <label for="password">Contraseña</label>
            <input type="password" id="password" name="password">

            <button type="submit">Iniciar sesión</button>
        </form>
    `;
});