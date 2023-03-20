import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { Router } from '@angular/router';
import { Client } from '../clients/client';

@Component({
  selector: 'app-addclient',
  templateUrl: './addclient.page.html',
  styleUrls: ['./addclient.page.scss'],
})
export class AddclientPage implements OnInit {

  public appPages = [
    { title: 'Chambres', url: '/chambres', icon: 'bed' },
    { title: 'Clients', url: '/clients', icon: 'people' },
    { title: 'Reservations', url: '/reservations', icon: 'accessibility' },
    { title: 'Factures', url: '/factures', icon: 'receipt' },
    { title: 'Statistiques', url: '/statistiques', icon: 'stats-chart' },
  ];
  
  clientForm!:FormGroup;

  constructor(private route: Router,private http:HttpClient, private formBuilder: FormBuilder) { }

  deconnexion() {
    this.route.navigate(['/login']);
  }

  ngOnInit() {
    this.clientForm=this.formBuilder.group({
      client:this.formBuilder.group({
        nom:[''],
        prenom:[''],
        telephone:['']
      })
    })
  }

  
  addClient() {
    this.http.post<Client>("http://localhost:3000/clients",this.clientForm.get('client')?.value);
  }
}
