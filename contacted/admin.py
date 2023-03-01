from django.contrib import admin
from contacted.models import contacted_detail

class contacted_details(admin.ModelAdmin):
    list_display = ["fullname", "email", "query"] 

admin.site.register(contacted_detail, contacted_details)    
