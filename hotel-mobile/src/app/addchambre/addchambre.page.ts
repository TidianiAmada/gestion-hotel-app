import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-addchambre',
  templateUrl: './addchambre.page.html',
  styleUrls: ['./addchambre.page.scss'],
})
export class AddchambrePage implements OnInit {

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
  
  addchambreformvalide() {
    
  }
}
