import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CreateGameComponent } from './components/create-game/create-game.component';
import { EditGameComponent } from './components/edit-game/edit-game.component';
import { GamesComponent } from './components/games/games.component';
import { AlbumComponent } from './components/album/album.component';


const routes: Routes = [
  { path: '', component: AlbumComponent },
  { path: 'crear-juego', component: CreateGameComponent },
  { path: 'editar-juego', component: EditGameComponent },
  { path: 'administrar-juegos', component: GamesComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
