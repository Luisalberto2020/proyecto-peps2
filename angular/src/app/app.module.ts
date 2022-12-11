import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { LoginComponent } from '../components/Registro/login/login.component';
import { RegistroCComponent } from '../components/Registro/registro-c/registro-c.component';
import { HomeComponent } from 'src/components/Registro/home/home.component';
import { ProductosComponent } from 'src/components/productos/productos/productos.component';
import { ListProductosComponent } from '../components/productos/list-productos/list-productos.component';
import { NavComponent } from '../components/productos/nav/nav.component';
import { ShopComponent } from '../components/productos/shop/shop.component';
import { AddProductoComponent } from '../components/productos/add-producto/add-producto.component';
import { NotFoundComponent } from '../components/not-found/not-found.component';





const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'registro', component: RegistroCComponent },
  { path: 'productos', component: ProductosComponent },
  {
    path: 'tienda',component:ShopComponent,
    children:[
      {path:'add',component:AddProductoComponent},
      {path:'',component:ListProductosComponent}
    ]
  },
  {path:'**',component:NotFoundComponent}
];


@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegistroCComponent,
    HomeComponent,
    ProductosComponent,
    ListProductosComponent,
    NavComponent,
    ShopComponent,
    AddProductoComponent,
    NotFoundComponent,
   
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(routes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
