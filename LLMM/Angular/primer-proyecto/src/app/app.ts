import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { UserCardComponent } from "./components/app-product-card/app-product-card";

@Component({
  selector: 'app-root',
  imports: [RouterOutlet,
    UserCardComponent],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('primer-proyecto');
}
