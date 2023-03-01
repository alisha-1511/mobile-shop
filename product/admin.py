from django.contrib import admin
from product.models import detail

class product_details(admin.ModelAdmin):
    list_display = ["img", "title", "price", "desc", "rating"] 

admin.site.register(detail, product_details)    
