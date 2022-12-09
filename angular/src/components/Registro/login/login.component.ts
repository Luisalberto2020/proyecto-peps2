import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {
mostrarFallo:Boolean = false;

  constructor(private router:Router) { }
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
        if (data.status === 200) {
          //this.router.navigate(['/home']);
          console.log(data);
        }else {
          this.mostrarFallo = true;
        }
      });
  }
  }
