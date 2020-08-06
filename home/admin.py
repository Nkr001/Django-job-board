from django.contrib import admin
from home.models import UserProfileInfo

# Register your models here.
from .models import Postjob
admin.site.register(Postjob)

admin.site.register(UserProfileInfo)