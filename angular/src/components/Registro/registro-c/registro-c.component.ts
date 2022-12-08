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



  registrar(event:Event,email:string, passwd:string,admin:boolean ){


    const options = {
        method: 'POST',
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({email, passwd, admin}),

    }
    console.log(options);
      fetch('http://localhost:5000/crear').then(res => res.json()).then(data => {
        if (data.status === 200) {
          this.router.navigate(['/login']);
        }else {
          this.mostrarFallo = true;
        }
      });
      event.preventDefault();
  }

}
