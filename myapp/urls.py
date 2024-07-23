from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('welcome/<str:password>/', views.welcome, name='welcome'),
    path('logout/', views.logout_view, name='logout'),
]
