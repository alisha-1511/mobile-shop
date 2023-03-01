from django.db import models

class detail(models.Model):
    img = models.ImageField(upload_to="product-images", height_field=None, width_field=None, max_length=None)
    title = models.CharField(max_length=50, default="Mobile")
    price = models.IntegerField()
    desc = models.TextField(max_length=250)
    rating = models.IntegerField()
    
