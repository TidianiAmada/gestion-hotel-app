import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AddchambrePage } from './addchambre.page';

const routes: Routes = [
  {
    path: '',
    component: AddchambrePage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class AddchambrePageRoutingModule {}
