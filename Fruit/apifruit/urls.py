from django.urls import path,include
from apifruit import views

urlpatterns = [
    path('Login', views.LoginView.as_view(), name="Login"),
    path('registration', views.register.as_view(), name="registration"),
    path('profile', views.profile.as_view(), name="profile"),
    path('changepassword', views.changepassword.as_view(), name="changepassword"),
    path('getall', views.allfruit.as_view(), name="allfruit"),
    path('<slug:name>', views.fruitnutrition.as_view(), name="fruitnutrition"),
]
