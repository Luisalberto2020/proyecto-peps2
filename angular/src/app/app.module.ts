import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { LoginComponent } from '../components/Registro/login/login.component';
import { RegistroCComponent } from '../components/Registro/registro-c/registro-c.component';
import { HomeComponent } from 'src/components/Registro/home/home.component';
import { ProductosComponent } from 'src/components/productos/productos/productos.component';



const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'registroc', component: RegistroCComponent },
  { path: 'productos', component: ProductosComponent },
];

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegistroCComponent,
    HomeComponent,
    ProductosComponent,
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(routes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
