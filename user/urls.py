from django.urls import path

from user.views import LoginView, ProfileView, RegisterView, UserRegisterationView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("user_register/", UserRegisterationView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/<str:id>/', ProfileView.as_view(), name='userProfile'),
]
