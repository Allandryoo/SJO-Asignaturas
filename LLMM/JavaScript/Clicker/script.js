const contador = document.querySelector("#contador");
const clickBtn = document.querySelector("#botonClicker");
const textMejora = document.querySelector(".mejoras h3")
const lvlUpBtn1 = document.querySelector("#mejora1");
const lvlUpBtn2 = document.querySelector("#mejora2");
const mensajeFinal = document.querySelector("#mensajeFinal")

clickBtn.style.backgroundColor = "lightgreen";
clickBtn.style.borderRadius = "999px";

lvlUpBtn1.style.backgroundColor = "lightyellow";
lvlUpBtn1.style.borderRadius = "999px";

lvlUpBtn2.style.backgroundColor = "lightyellow";
lvlUpBtn2.style.borderRadius = "999px";

let count = 0;
let multi = 10000;

clickBtn.addEventListener("click", () => {
    count += multi;
    contador.textContent = count;
    if (count >= 10000) {
        clickBtn.style.display = "none";
        lvlUpBtn1.style.display = "none";
        lvlUpBtn2.style.display = "none";
        textMejora.style.display = "none"
        mensajeFinal.textContent = "¡Felicidades! Has llegado al máximo!";
    }
});

lvlUpBtn1.addEventListener("click", () => {
    if (count >= 200) {
        count -= 200;
        multi *= 2;
        contador.textContent = count;
    }
});

lvlUpBtn2.addEventListener("click", () => {
    if (count >= 1000) {
        count -= 1000;
        multi *= 4;
        contador.textContent = count;
    }
});