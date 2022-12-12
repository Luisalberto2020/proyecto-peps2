export class Producto{
    id: number;
    nombre: string;
    precio: number;
    url:string;

    constructor(id: number, nombre: string, precio: number,url:string){
        this.id = id;
        this.nombre = nombre;
        this.precio = precio;
        this.url = url;

    }
}
