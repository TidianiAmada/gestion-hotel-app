import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
})
export class LoginPage implements OnInit {

  public email !: string;
  public mdp !: string;
  
  constructor(private route: Router) {}

  ngOnInit() {}

  login() {
    this.route.navigate(['/chambres']);
    //if (this.email == undefined || this.mdp == undefined) {
    //  this.myalert("Veillez tapez votre email et votre mot de passe !");
    //  //alert("Veillez tapez votre email et votre mot de passe !");
    //} else {
    //  if (this.email == "seyni" && this.mdp == "passer") {
    //    this.route.navigate(['/folder/Inbox']);
    //  } else {
    //    this.myalert("Email ou Mot de passe incorrect !");
    //  }
    //}
  }

  async myalert(msg: string) {
    const alert = document.createElement('ion-alert');
    alert.subHeader = msg;
    alert.buttons = ['OK'];
    document.body.appendChild(alert);
    await alert.present();
  }
}
