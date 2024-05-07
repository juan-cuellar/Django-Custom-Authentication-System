from django.urls import path
from .views import Login, Register, logout, Index

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('index/', Index.as_view(), name='index')
]