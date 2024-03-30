
from django.contrib.auth.models import AbstractUser
from django.db import models

class utilisateurs(AbstractUser):
# faire savoir a django que c'est cette classe qu'il faut utiliser pour le modele utilisatuer
# il faut aller faire dans settings.py ligne 132
    phone = models.CharField(max_length=13,unique=True,null=True,blank=True)
    profile=models.ImageField(upload_to='profile/',null=True,blank=True)
    token = models.CharField(max_length=120, default='')
    

# Create your models here.
