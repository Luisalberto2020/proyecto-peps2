import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { LoginComponent } from '../components/Registro/login/login.component';
import { RegistroCComponent } from '../components/Registro/registro-c/registro-c.component';
import { HomeComponent } from 'src/components/Registro/home/home.component';



const routes: Routes = [
  { path: 'login', component: LoginComponent },
];

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegistroCComponent,
    HomeComponent,
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(routes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
