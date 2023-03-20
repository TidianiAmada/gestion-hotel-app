import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { UpdateclientPageRoutingModule } from './updateclient-routing.module';

import { UpdateclientPage } from './updateclient.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    UpdateclientPageRoutingModule
  ],
  declarations: [UpdateclientPage]
})
export class UpdateclientPageModule {}
