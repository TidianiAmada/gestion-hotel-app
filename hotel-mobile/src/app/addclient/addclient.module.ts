import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import {HttpClientModule} from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';

import { AddclientPageRoutingModule } from './addclient-routing.module';

import { AddclientPage } from './addclient.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    AddclientPageRoutingModule,
    HttpClientModule,
    ReactiveFormsModule
  ],
  declarations: [AddclientPage]
})
export class AddclientPageModule {}
