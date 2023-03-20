import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AddreservationPage } from './addreservation.page';

const routes: Routes = [
  {
    path: '',
    component: AddreservationPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class AddreservationPageRoutingModule {}
