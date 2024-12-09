from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('admin', 'Admin'),
        ('supervisor', 'Supervisor'),
        ('worker', 'Worker'),
    )
    
    user_type = models.CharField(max_length=100, choices=USER_TYPES)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, unique=True, default='Jeffy')
    image=models.ImageField(upload_to='profileimages/' ,default='default.jpg')
    phone=models.IntegerField(default='07546372', blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name', 'image', 'phone' ]
    
    class Meta:
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.username
    


