from django.db import models

class contacted_detail(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    query = models.TextField()
   
    