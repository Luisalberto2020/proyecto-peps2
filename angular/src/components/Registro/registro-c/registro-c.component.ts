import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-registro-c',
  templateUrl: './registro-c.component.html',
  styleUrls: ['./registro-c.component.scss']
})
export class RegistroCComponent {
  mostrarFallo:Boolean = false;
  constructor(private router: Router) { }



  registrar(event:Event,email:string, password:string,admin:boolean ){


    const options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*"
        },
        body: JSON.stringify({email, password, admin}),

    }
    console.log(options);
      fetch('http://localhost:5000/crearusuario',options).then(res => res.json()).then(data => {
        if (data.code === 200) {
          this.router.navigate(['/login']);
        }else {
          this.mostrarFallo = true;
        }
      });
  }

}
