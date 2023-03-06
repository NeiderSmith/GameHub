import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { RestService } from 'src/app/services/rest.service';

@Component({
  selector: 'app-album',
  templateUrl: './album.component.html',
  styleUrls: ['./album.component.css']
})
export class AlbumComponent {

  messageOk = null;
  messageErr = null;
  closeResult = '';

  no_disponible = "https://dynamicmediainstitute.org/wp-content/themes/dynamic-media-institute/imagery/default-book.png";

  games = [{
    title: "",
    description: "",
    release_date: "",
    category: {name:""},
    cover_image: "",
  }]

  constructor(private rest: RestService, private route: Router) { }

  ngOnInit(): void {
    this.getGames();
  }

  async getGames() {
    var res = await this.rest.GetRequest('games/active').toPromise();
    this.games = res;
  }

  cerrarAlert1() {
    this.messageOk = null;
  }

  cerrarAlert2() {
    this.messageErr = null;
  }

}
