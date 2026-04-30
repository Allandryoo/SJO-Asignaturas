import { Component, signal } from '@angular/core';

@Component({
  selector: 'app-perfil',
  imports: [],
  templateUrl: './perfil.html',
  styleUrl: './perfil.css',
})
export class PerfilCardComponent {
  nombre = signal("ana");
  edad = signal(22);
  imagen = signal('anaFrozen.png');

  cumplirAnio() {
    this.edad.update(e => e + 1);
  }
}
