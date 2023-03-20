import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { ChambresPageRoutingModule } from './chambres-routing.module';

import { ChambresPage } from './chambres.page';

import { MenuComponent } from '../menu/menu.component';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    ChambresPageRoutingModule
  ],
  declarations: [ChambresPage, MenuComponent]
})
export class ChambresPageModule {}
