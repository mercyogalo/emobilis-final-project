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
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]
    
    class Meta:
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.username
    


