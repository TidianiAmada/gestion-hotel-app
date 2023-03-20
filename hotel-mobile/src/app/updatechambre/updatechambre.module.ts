import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { UpdatechambrePageRoutingModule } from './updatechambre-routing.module';

import { UpdatechambrePage } from './updatechambre.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    UpdatechambrePageRoutingModule
  ],
  declarations: [UpdatechambrePage]
})
export class UpdatechambrePageModule {}
