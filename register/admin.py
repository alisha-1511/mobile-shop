from django.contrib import admin
from register.models import user_detail

# Register your models here.
class user(admin.ModelAdmin):
    list_display = ["fullname", "email", "password", "number", "address"]
    
admin.site.register(user_detail, user)    
