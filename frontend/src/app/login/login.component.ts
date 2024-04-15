import { Component } from '@angular/core';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})

export class LoginComponent {
  email: string = '';
  otp: number = 0;
  showOtpInput: boolean = false;

  constructor(private authService: AuthService, private router: Router) { }

  generateOtp(email: string) {
    this.authService.generateOtp(email)
      .then(response => {
        console.log(response.data);
        this.showOtpInput = true;
      })
      .catch(error => {
        console.error(error);
      });
  }

  verifyOtp(email: string, otp:number) {
    this.authService.verifyOtp(email, otp)
      .then(response => {
        this.router.navigate(['dashboard']);
      })
      .catch(error => {
        console.error(error);
      })
  }
}
