from django.urls import path
from .views import login, register, forgot, reset, activate, logout, profile

urlpatterns = [
    path('', login, name='home'),
    path('', login, name='login'),
    path('register/', register, name='register'),
    path('forgot/', forgot, name='forgot'),
    path('reset/', reset, name='reset'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('activate/<uidb64>/<token>/', activate, name='activate')
]