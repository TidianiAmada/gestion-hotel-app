import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.scss'],
})
export class MenuComponent  implements OnInit {
  public appPages = [
    { title: 'Chambres', url: '/chambres', icon: 'bed' },
    { title: 'Clients', url: '/clients', icon: 'people' },
    { title: 'Reservations', url: '/reservations', icon: 'accessibility' },
    { title: 'Factures', url: '/factures', icon: 'receipt' },
    { title: 'Statistiques', url: '/statistiques', icon: 'stats-chart' },
  ];
  constructor(private route: Router) { }

  ngOnInit() { }
  
  deconnexion() {
    this.route.navigate(['/login']);
  }

}
