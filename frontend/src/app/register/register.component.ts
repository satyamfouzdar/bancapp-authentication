import { Component } from '@angular/core';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [],
  templateUrl: './register.component.html',
  styleUrl: './register.component.css'
})
export class RegisterComponent {

  constructor(private authService: AuthService, private router: Router) { }

  signUp(email: string, fullName: string) {
    this.authService.signUp(email, fullName)
      .then(response => {
        console.log(response.data);
        this.router.navigate(['/login']);
      })
      .catch(error => {
        console.error(error);
      });
  }
}
