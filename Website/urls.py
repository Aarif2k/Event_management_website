
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name="index"),
    path("booking",views.booking,name="booking"),
    path("register",views.register,name="register"),
    path("login",views.login_2,name="login"),
    path("logout",views.logout,name="logout"),
]