import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { Client } from './client';
import { Observable } from 'rxjs';
import { FormBuilder, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-clients',
  templateUrl: './clients.page.html',
  styleUrls: ['./clients.page.scss'],
})
export class ClientsPage implements OnInit {
  public appPages = [
    { title: 'Chambres', url: '/chambres', icon: 'bed' },
    { title: 'Clients', url: '/clients', icon: 'people' },
    { title: 'Reservations', url: '/reservations', icon: 'accessibility' },
    { title: 'Factures', url: '/factures', icon: 'receipt' },
    { title: 'Statistiques', url: '/statistiques', icon: 'stats-chart' },
  ];
  clients!:Client[];

  deconnexion() {
    this.route.navigate(['/login']);
  }
  constructor(private route: Router,private http:HttpClient, private formBuilder: FormBuilder) { 
    
  }


  ngOnInit() {
    this.clientlist().subscribe();
    
  }

  clientlist():Observable<Client[]> {
    return this.http.get<Client[]>("http://localhost:3000/clients");
  }

  addclientform() {
  
    this.route.navigate(['/addclient']);
  }
  
  
  updateclientform() {
    this.route.navigate(['/updateclient']);
  }

  deleteclient() {
    
  }

}
