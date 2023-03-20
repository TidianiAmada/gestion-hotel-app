import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { FacturesPage } from './factures.page';

const routes: Routes = [
  {
    path: '',
    component: FacturesPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class FacturesPageRoutingModule {}
