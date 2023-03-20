import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { StatistiquesPageRoutingModule } from './statistiques-routing.module';

import { StatistiquesPage } from './statistiques.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    StatistiquesPageRoutingModule
  ],
  declarations: [StatistiquesPage]
})
export class StatistiquesPageModule {}
