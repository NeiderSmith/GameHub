import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { RestService } from 'src/app/services/rest.service';

@Component({
  selector: 'app-edit-game',
  templateUrl: './edit-game.component.html',
  styleUrls: ['./edit-game.component.css']
})
export class EditGameComponent {
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
    this.loadGame();
  }
  
  async loadGame() {
    var id = sessionStorage.getItem('id');
    var res = await this.rest.GetRequest('games/' + id).toPromise();
    res = res;
    this.game.title = res.title;
    this.game.description = res.description;
    this.game.category_id = res.category_id;
    this.game.release_date = res.release_date;
    this.game.cover_image = res.cover_image;
    this.game.active = res.active;
    this.cover_image = res.cover_image;
  }

  uploadImagen(event: any) {
    if (event.target.files && event.target.files[0]) {
      var file = event.target.files[0];
      const reader = new FileReader();
      reader.onload = e => this.cover_image = reader.result;
      reader.readAsDataURL(file);
    }
  }

  async actualizar() {
    
    this.game.cover_image = this.cover_image;

    var id = sessionStorage.getItem('id');

    try {
      var res = await this.rest.PutRequest('games/' + id, this.game).toPromise();
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
