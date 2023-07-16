from django.contrib.auth.decorators import login_required
from django.urls import path

from users.views import (EmailVerificationView, UserProfileView,
                         UserRegistrationView, login, logout)

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', logout, name='logout'),
    path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),
]
