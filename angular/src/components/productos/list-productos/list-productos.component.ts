import { Component, OnInit } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';
import { Producto } from 'src/model/Producto';

@Component({
  selector: 'app-list-productos',
  templateUrl: './list-productos.component.html',
  styleUrls: ['./list-productos.component.scss']
})
export class ListProductosComponent implements OnInit {
  poductos: Producto[] = [];

  constructor(private cookies:CookieService) { }

  ngOnInit(): void {
    const options = {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Token':  this.cookies.get('token'),
        'Access-Control-Allow-Origin': '*',
      },
    };
    fetch('http://localhost:3000/getproductos', options).then(res => res.json()).then(data => {
      for (let i = 0; i < data.length; i++) {
        this.poductos.push(new Producto(data[i].id, data[i].nombre, data[i].precio));
      }

    });
  }

}


