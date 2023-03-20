import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { AddchambrePageRoutingModule } from './addchambre-routing.module';

import { AddchambrePage } from './addchambre.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    AddchambrePageRoutingModule
  ],
  declarations: [AddchambrePage]
})
export class AddchambrePageModule {}
