import { Component, signal } from '@angular/core';

@Component({
  selector: 'app-user-card',
  standalone: true,
  templateUrl: './app-product-card.html',
  styleUrls: [`./app-product-card.css`]
})
export class UserCardComponent {
  nombreProducto = signal('Monitor');
  precio = signal('150,00€');
  ciudad = signal('Madrid');
}

