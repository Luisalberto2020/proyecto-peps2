import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {
mostrarFallo:Boolean = false;

  constructor(private router:Router,private cookies:CookieService) { }
  loguearse(email:string, password:string ){
    const options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*"
        },
        body: JSON.stringify({email, password}),

    }
    console.log(options);
      fetch('http://localhost:5000/loginusuario',options).then(res => res.json()).then(data => {
        if (data.code === 200) {
          this.cookies.set("token",data.token)
          this.router.navigate(['tienda']);
        }else {
          this.mostrarFallo = true;
        }
      });
  }
  }
