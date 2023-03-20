import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { StatistiquesPage } from './statistiques.page';

const routes: Routes = [
  {
    path: '',
    component: StatistiquesPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class StatistiquesPageRoutingModule {}
