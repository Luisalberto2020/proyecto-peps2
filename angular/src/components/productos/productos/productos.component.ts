import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';
import { Producto } from 'src/model/Producto';


@Component({
  selector: 'app-productos',
  templateUrl: './productos.component.html',
  styleUrls: ['./productos.component.scss']
})
export class ProductosComponent implements OnInit {
  @Input() producto:Producto = new Producto(1,'',1,'');
  @Input() index:number = 0;
  @Input() admin:boolean = false;
  @Output() deleteRequest = new EventEmitter<number>();
  url2:string = '';

  constructor(private cookies:CookieService,private route:Router) { }
  ngOnInit(): void {
    this.url2= 'http://localhost:5000/getfoto/'+this.producto.url;
  }

  eliminarProducto(){
    const options = {
      method: 'DELETE',
      headers: {
        "Access-Control-Allow-Origin": "*",
        "token" : this.cookies.get('token'),
      },
  }
  console.log(options);
  console.log(this.producto.id);
  fetch('http://localhost:5000/deleteproducto/'+this.producto.id, options).then(res => res.json()).then(data => {
      //TODO: Eliminar el producto de la lista
      if (data.status == 200) {
        this.deleteRequest.emit(this.index);
      }else {
        console.log(data);
      }


    });
}
updateProducto(){
  this.route.navigate(['/tienda/update/'+this.producto.id]);
}

}

