from django.urls import path 
from . import views
app_name = 'authentication'
urlpatterns = [
    path('', views.login_, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_, name='logout')
]
