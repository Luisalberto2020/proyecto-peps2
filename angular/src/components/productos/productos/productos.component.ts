import { Component, Input } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';
import { Producto } from 'src/model/Producto';


@Component({
  selector: 'app-productos',
  templateUrl: './productos.component.html',
  styleUrls: ['./productos.component.scss']
})
export class ProductosComponent {
  @Input() producto:Producto = new Producto(1,'',1,'');
  @Input() index:number = 0;
  @Input() admin:boolean = false;

  constructor(private cookies:CookieService) { }

  eliminarProducto(){
    const options = {
      method: 'DELETE',
      headers: {
        "Access-Control-Allow-Origin": "*",
        "token" : this.cookies.get('token'),
      },
  }
  console.log(options);
  fetch('http://localhost:5000/deleteproducto/'+this.producto.id, options).then(res => res.json()).then(data => {
      //TODO: Eliminar el producto de la lista

    });
}

}

