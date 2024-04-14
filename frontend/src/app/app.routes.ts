import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { DashboardComponent } from './dashboard/dashboard.component';

export const routes: Routes = [
  { path: '', component: DashboardComponent }, // Dashboard as the root path
  { path: 'login', component: LoginComponent },
  { path: 'signup', component: RegisterComponent },
  { path: '**', redirectTo: '' }
];