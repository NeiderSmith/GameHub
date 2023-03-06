import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { RestService } from 'src/app/services/rest.service';

@Component({
  selector: 'app-create-game',
  templateUrl: './create-game.component.html',
  styleUrls: ['./create-game.component.css']
})
export class CreateGameComponent {
  no_disponible = "https://dynamicmediainstitute.org/wp-content/themes/dynamic-media-institute/imagery/default-book.png";
  cover_image: any = null;

  game = {
    title: "",
    description: "",
    release_date: "",
    cover_image: null,
    category_id: "",
    active: ""
  };

  messageOk = null;
  messageErr = null;

  constructor(private rest: RestService, private route: Router) { }

  ngOnInit(): void {
  }

  uploadImagen(event: any) {
    if (event.target.files && event.target.files[0]) {
      var file = event.target.files[0];
      const reader = new FileReader();
      reader.onload = e => this.cover_image = reader.result;
      reader.readAsDataURL(file);
    }
  }

  async agregar() {
    // obtener imagen
    this.game.cover_image = this.cover_image;
    // mostrar datos
    console.log(this.game.title)
    console.log(this.game.description)
    console.log(this.game.category_id)

    try {
      // peticion
      // podemos utilizar await o no
      var res = await this.rest.PostRequest("games", this.game).toPromise();
      this.messageOk = res.message;
      this.regresar();

    } catch (error: any) {
      this.messageErr = error.error.message
    }
  }

  regresar() {
    this.route.navigate(["administrar-juegos"])
  }

  cerrarAlert1() {
    this.messageOk = null;
  }

  cerrarAlert2() {
    this.messageErr = null;
  }
}
