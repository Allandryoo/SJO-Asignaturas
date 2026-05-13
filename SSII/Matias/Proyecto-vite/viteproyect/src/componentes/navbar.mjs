export function Navbar() {
    return `
<nav class="navbar">
<div class="logo">Mi Sitio</div>
<ul class="nav-links">
<li><a href="#section1">Inicio</a></li>
<li><a href="#section2">Servicios</a></li>
<li><a href="#section3">Contacto</a></li>
</ul>
<div class="botonBurguer" id="mobileBurguer">
<span class="bar"></span>
<span class="bar"></span>
<span class="bar"></span>
</div>
</nav>
`;
}
export function navbarStyles() {
    return `
.navbar {
display: flex;
justify-content: space-between;
align-items: center;
padding: 1rem 2rem;
background-color: #333;
color: #fff;
}
.navbar .logo { font-size: 1.5rem; }
.navbar .nav-links { list-style: none; display: flex; }
.navbar .nav-links li { margin-left: 1rem; }
.navbar .nav-links a { color: #fff; text-decoration: none; }
.navbar .botonBurguer { display: none; flex-direction: column; cursor: pointer; }
.navbar .bar { height: 3px; width: 25px; background-color: #fff; margin: 4px 0;
transition: all 0.3s ease; }
@media (max-width: 768px) {
.navbar .nav-links { display: none; flex-direction: column; width: 100%; text-align:
center; }
.navbar .nav-links.active { display: flex; }
.navbar .botonBurguer { display: flex; }
}
`;
}