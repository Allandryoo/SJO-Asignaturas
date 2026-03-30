const countElement = document.getElementById('count');
const clickBtn = document.getElementById('click-btn');
const lvlUpBtn = document.getElementById('reset-btn');
//const lvlUpBtnPlus =
let count = 0;

clickBtn.addEventListener('click', () => {
    count++;
});

resetBtn.addEventListener('click', () => {
    count = 0;
});
