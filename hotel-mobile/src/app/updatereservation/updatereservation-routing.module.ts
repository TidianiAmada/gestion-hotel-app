import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { UpdatereservationPage } from './updatereservation.page';

const routes: Routes = [
  {
    path: '',
    component: UpdatereservationPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class UpdatereservationPageRoutingModule {}
