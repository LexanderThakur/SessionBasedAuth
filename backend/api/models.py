from django.db import models

# Create your models here.

class User(models.Model):

    user_email=models.EmailField(unique=True)
    user_password= models.CharField(max_length=255)
    create_at= models.DateField(auto_now_add=True)

class Session(models.Model):
    session_id=models.CharField(max_length=255,unique=True)
    user_email=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at= models.DateField(auto_now_add=True)

