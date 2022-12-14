import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-update-producto',
  templateUrl: './update-producto.component.html',
  styleUrls: ['./update-producto.component.scss']
})
export class UpdateProductoComponent implements OnInit {
  id:number = 0;
  nombre:string = '';
  precio:number = 0;
  url:string = '';

  constructor(private route:ActivatedRoute,private cookies:CookieService) { }
  ngOnInit(): void {
    this.id = this.route.snapshot.params['id'];
    const options = {
      method: 'GET',
      headers: {
          'token': this.cookies.get('token'),
      },
    };
    fetch('http://localhost:5000/getproducto/'+this.id,options).then(res => res.json()).then(data => {
      this.nombre = data.nombre;
      this.precio = data.precio;
    });
}



  updateProducto(){


    const options = {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Token': this.cookies.get('token'),
        'Access-Control-Allow-Origin': '*',
      },
    body: JSON.stringify({id:this.id,nombre:this.nombre, precio:this.precio,url:this.url}),
    }
    fetch('http://localhost:5000/updateproducto/',options).then(res => res.json()).then(data => {
      const toastLiveExample = document.getElementById('liveToast')
      toastLiveExample?.classList.add('show');


    });
  }
  subirfoto() {
    console.log(this.id);

    const fileInput = document.getElementById('fotoinput') as HTMLInputElement;
    const file = fileInput?.files?.[0];
    console.log(file);


    if (file != null) {
    const formData = new FormData();

    formData.append('file', file);

    // Enviar el archivo al servidor utilizando fetch
    fetch('http://localhost:5000/subirfoto/'+this.id, {
      method: 'POST',
      body: formData,
      headers: {
        'Token': this.cookies.get('token'),
        'Access-Control-Allow-Origin': '*',
      }

    })
      .then(response => {
        // La respuesta del servidor será enviada aquí
        alert('Foto subida correctamente');
      })


  }
  }

}


