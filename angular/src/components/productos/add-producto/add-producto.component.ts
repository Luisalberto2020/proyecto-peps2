import { Component } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-add-producto',
  templateUrl: './add-producto.component.html',
  styleUrls: ['./add-producto.component.scss']
})
export class AddProductoComponent {
  nombre: string = '';
  precio: string = '';
  url: string = '';


  constructor(private cokies: CookieService) { }


  addProducto() {

    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Token': this.cokies.get('token'),
        'Access-Control-Allow-Origin': '*',
      },
      body: JSON.stringify({ nombre: this.nombre, precio: this.precio }),
    }
    fetch('http://localhost:5000/crearproducto', options).then(res => res.json()).then(data => {
      console.log(data);
      if (data.code == 200) {
        console.log('Producto creado');
        alert('Producto creado correctamente');

      }

    });


  }
  subirfoto() {
    const fileInput = document.getElementById('fileInput') as HTMLInputElement;
    const file = fileInput?.files?.[0];


    if (file != null) {
    const formData = new FormData();

    formData.append('file', file);

    // Enviar el archivo al servidor utilizando fetch
    fetch('http://localhost:5000/subirfoto/<id>', {
      method: 'POST',
      body: formData,
      headers: {
        'Token': this.cokies.get('token'),
        'Access-Control-Allow-Origin': '*',
      }

    })
      .then(response => {
        // La respuesta del servidor será enviada aquí
        console.log(response);
        alert('Foto subida correctamente');
        const toastLiveExample = document.getElementById('liveToast')
        toastLiveExample?.classList.add('show');
      })


  }
  }

}
