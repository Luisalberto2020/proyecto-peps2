import { Component } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-add-producto',
  templateUrl: './add-producto.component.html',
  styleUrls: ['./add-producto.component.scss']
})
export class AddProductoComponent {
  nombre:string = '';
  precio:string = '';
  url:string = '';

  constructor(private cokies:CookieService) { }


  addProducto(){

    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Token': this.cokies.get('token'),
        'Access-Control-Allow-Origin': '*',
      },
      body: JSON.stringify({nombre:this.nombre, precio:this.precio, url:this.url}),
    }
    fetch('http://localhost:5000/addproductos', options).then(res => res.json()).then(data => {
      console.log(data);
    });

  }


}
