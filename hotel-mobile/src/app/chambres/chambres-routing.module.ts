import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ChambresPage } from './chambres.page';

const routes: Routes = [
  {
    path: '',
    component: ChambresPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class ChambresPageRoutingModule {}
