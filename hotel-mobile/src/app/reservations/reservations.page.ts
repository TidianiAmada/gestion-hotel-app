import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-reservations',
  templateUrl: './reservations.page.html',
  styleUrls: ['./reservations.page.scss'],
})
export class ReservationsPage implements OnInit {

  public appPages = [
    { title: 'Chambres', url: '/chambres', icon: 'bed' },
    { title: 'Clients', url: '/clients', icon: 'people' },
    { title: 'Reservations', url: '/reservations', icon: 'accessibility' },
    { title: 'Factures', url: '/factures', icon: 'receipt' },
    { title: 'Statistiques', url: '/statistiques', icon: 'stats-chart' },
  ];

  deconnexion() {
    this.route.navigate(['/login']);
  }
  constructor(private route: Router) { }

  ngOnInit() {
  }

  addreservationform() {
    this.route.navigate(['/addreservation']);
  }
  
  updatereservationform() {
    this.route.navigate(['/updatereservation']);
  }

  deletereservation() {
    
  }

}
