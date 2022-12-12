import { Component, Input } from '@angular/core';
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

  eliminarProducto(id:number, index:number){
    const options = {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        "Access-Control-Allow-Origin": "*"
      },
      body: JSON.stringify({id}),
  }
  console.log(options);
  fetch('http://localhost:5000/deleteproductos', options).then(res => res.json()).then(data => {
      //TODO: Eliminar el producto de la lista
      
    });
}

}

