from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MatthermostAuth(models.Model):
    login_id= models.EmailField(unique=True,null=False)
    password=models.CharField(null=False, max_length=254)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=False)

    def __str__(self):
        return self.login_id