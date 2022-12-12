import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.scss']
})
export class NavComponent {
  constructor(private cookies:CookieService,private router:Router) { }
  cerrarSesion(){
    this.cookies.delete("token");
    this.router.navigate([""]);

  }
}
