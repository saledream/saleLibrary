from django.contrib import admin
from .models import UserProfile,DownloadBook 

# Register your models here.


@admin.register(UserProfile)

class UserProfileAdmin(admin.ModelAdmin):
    pass 



@admin.register(DownloadBook)

class UserProfileAdmin(admin.ModelAdmin):
    pass