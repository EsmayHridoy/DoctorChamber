from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

# Create your models here.

class Role(models.Model):
    role = models.CharField(max_length=100)
    def __str__(self):
        return self.role

class User(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 


    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

