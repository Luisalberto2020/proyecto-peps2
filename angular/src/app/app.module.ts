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
import { CookieService } from 'ngx-cookie-service';
import { LoginGuard } from 'src/Guards/LoginGuard';
import { FormsModule } from '@angular/forms';
import { UpdateProductoComponent } from '../components/productos/update-producto/update-producto.component';





const routes: Routes = [
  {
     path: '', component: HomeComponent,
      children: [
        { path: '', component: LoginComponent },
        { path: 'registro', component: RegistroCComponent }
      ]
    },
  {
    path: 'tienda',component:ShopComponent,
    children:[
      {path:'add',component:AddProductoComponent},
      {path:'',component:ListProductosComponent},
      {path:'update/:id',component:UpdateProductoComponent}
    ],
    canActivate:[LoginGuard]
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
    UpdateProductoComponent,

  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(routes),
    FormsModule,

  ],
  providers: [CookieService,LoginGuard],
  bootstrap: [AppComponent]
})
export class AppModule { }
