from django.db import models

class user_detail(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    number = models.IntegerField()
    address = models.CharField(max_length=150)