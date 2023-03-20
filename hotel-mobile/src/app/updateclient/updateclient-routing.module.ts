import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { UpdateclientPage } from './updateclient.page';

const routes: Routes = [
  {
    path: '',
    component: UpdateclientPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class UpdateclientPageRoutingModule {}
