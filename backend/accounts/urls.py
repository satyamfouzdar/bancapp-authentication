from django.urls import path

from accounts.views import UserView, SignUpView, LoginView, VerifyOTPView


urlpatterns = [
    path('', UserView.as_view()),
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('login/verify/', VerifyOTPView.as_view()),
]