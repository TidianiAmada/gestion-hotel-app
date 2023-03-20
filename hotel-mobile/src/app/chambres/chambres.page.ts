import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-chambres',
  templateUrl: './chambres.page.html',
  styleUrls: ['./chambres.page.scss'],
})
export class ChambresPage implements OnInit {
  public appPages = [
    { title: 'Chambres', url: '/chambres', icon: 'bed' },
    { title: 'Clients', url: '/clients', icon: 'people' },
    { title: 'Reservations', url: '/reservations', icon: 'accessibility' },
    { title: 'Factures', url: '/factures', icon: 'receipt' },
    { title: 'Statistiques', url: '/statistiques', icon: 'stats-chart' },
  ];

  constructor(private route: Router) { }
  
  deconnexion() {
    this.route.navigate(['/login']);
  }

  ngOnInit() {
  }

  
  addchambreform() {
    this.route.navigate(['/addchambre']);
  }
  
  updatechambreform() {
    this.route.navigate(['/updatechambre']);
  }

  deletechambre() {
    
  }
}
