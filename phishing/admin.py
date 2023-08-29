from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Credentials
# Register your models here.

class CredentialsModelAdmin(ModelAdmin):
    list_display= ['username','password','created_at']
    # class Meta:
        
admin.site.register(Credentials,CredentialsModelAdmin)