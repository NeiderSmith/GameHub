import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { RestService } from 'src/app/services/rest.service';

@Component({
  selector: 'app-games',
  templateUrl: './games.component.html',
  styleUrls: ['./games.component.css']
})
export class GamesComponent {

  messageOk = null;
  messageErr = null;

  constructor(private rest: RestService, private route: Router) { }

  games = [{
    id: 0,
    title: "",
    description: "",
    release_date: "",
    category: {name:""},
    cover_image: "",
    active: 0,
  }]

  ngOnInit(): void {
    this.getGames();
  }

  async getGames() {
    var res = await this.rest.GetRequest('games').toPromise();
    this.games = res;
  }

  getValue(bool: any) {
    if (bool == true) {
      return "Si"
    } else {
      return "No"
    }

  }
  
  editar(i: any) {
    console.log("entro");
    var game: any = this.games[i];
    sessionStorage.setItem('id', game.id);
    this.route.navigate(["editar-juego"]);
  }

  async eliminar(i: any) {
    var game: any = this.games[i];
    try {
      var res = await this.rest.DeleteRequest('games/' + game.id).toPromise();
      this.messageOk = res.message;
      this.getGames();
    } catch (error: any) {
      this.messageErr = error.error.message;
    }
  }

  cerrarAlert1() {
    this.messageOk = null;
  }

  cerrarAlert2() {
    this.messageErr = null;
  }


}
