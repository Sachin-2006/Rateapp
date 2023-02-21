from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name = "home"),
    path('profile/<str:sname>',profile,name = "profile"),
    path('login/',login_user,name = 'login'),
    path('logout/',logout_user,name='logout')
]