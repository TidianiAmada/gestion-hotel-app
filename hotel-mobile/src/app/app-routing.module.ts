import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'login',
    pathMatch: 'full'
  },
  {
    path: 'login',
    loadChildren: () => import('./login/login.module').then( m => m.LoginPageModule)
  },
  {
    path: 'chambres',
    loadChildren: () => import('./chambres/chambres.module').then( m => m.ChambresPageModule)
  },
  {
    path: 'clients',
    loadChildren: () => import('./clients/clients.module').then( m => m.ClientsPageModule)
  },
  {
    path: 'reservations',
    loadChildren: () => import('./reservations/reservations.module').then( m => m.ReservationsPageModule)
  },
  {
    path: 'factures',
    loadChildren: () => import('./factures/factures.module').then( m => m.FacturesPageModule)
  },
  {
    path: 'statistiques',
    loadChildren: () => import('./statistiques/statistiques.module').then( m => m.StatistiquesPageModule)
  },
  {
    path: 'addchambre',
    loadChildren: () => import('./addchambre/addchambre.module').then( m => m.AddchambrePageModule)
  },
  {
    path: 'updatechambre',
    loadChildren: () => import('./updatechambre/updatechambre.module').then( m => m.UpdatechambrePageModule)
  },
  {
    path: 'addclient',
    loadChildren: () => import('./addclient/addclient.module').then( m => m.AddclientPageModule)
  },
  {
    path: 'updateclient',
    loadChildren: () => import('./updateclient/updateclient.module').then( m => m.UpdateclientPageModule)
  },
  {
    path: 'updatereservation',
    loadChildren: () => import('./updatereservation/updatereservation.module').then( m => m.UpdatereservationPageModule)
  },
  {
    path: 'addreservation',
    loadChildren: () => import('./addreservation/addreservation.module').then( m => m.AddreservationPageModule)
  }
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule {}
