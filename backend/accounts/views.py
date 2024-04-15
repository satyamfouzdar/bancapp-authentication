import random
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import User


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if email:
            user = get_object_or_404(User, email=email)
            otp = random.randint(1000, 9999)  # Generate OTP
            user.login_otp = otp
            user.save()
            send_mail(
                'OTP for Login',
                f'Your OTP is: {otp}',
                'from@example.com',
                [email],
                fail_silently=False,
            )
            return Response({'message': 'OTP sent to your email'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTPView(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')
        if email and otp:
            user = get_object_or_404(User, email=email)
            if otp == user.login_otp:
                refresh = RefreshToken.for_user(user)
                return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Email and OTP are required'}, status=status.HTTP_400_BAD_REQUEST)


class SignUpView(APIView):
    def post(self, request):
        try:
            email = request.data['email']
            full_name = request.data['fullName']
        except:
            return Response({'message': 'Complete Data Required'}, status=status.HTTP_400_BAD_REQUEST)

        user_exists_already = User.objects.filter(email=email).exists()

        if user_exists_already:
            return Response({'message': 'User with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(
            email=email,
            full_name=full_name
        )

        return Response({'message': "User created sucessfully."})

class UserView(APIView):
    def get(self, request):
        return Response({'success': True})
