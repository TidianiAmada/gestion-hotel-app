import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { UpdatereservationPageRoutingModule } from './updatereservation-routing.module';

import { UpdatereservationPage } from './updatereservation.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    UpdatereservationPageRoutingModule
  ],
  declarations: [UpdatereservationPage]
})
export class UpdatereservationPageModule {}
