from django.urls import path
from core import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view, name='login'),
]
