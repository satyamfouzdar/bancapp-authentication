import { Injectable } from '@angular/core';
import axios from 'axios';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor() { }

  signUp(email: string, fullName: string) {
    console.log("I am here")
    return axios.post('http://localhost:8000/api/v1/accounts/signup/', { email, fullName });
  }

  generateOtp(email: string) {
    console.log("Login")
    return axios.post('http://localhost:8000/api/v1/accounts/login/', { email});
  }

  verifyOtp(email: string, otp: number) {
    console.log("Login")
    return axios.post('http://localhost:8000/api/v1/accounts/login/verify/', { email, otp})
  }
}