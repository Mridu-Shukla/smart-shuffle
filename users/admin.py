from django.contrib import admin
from users.models import UserProfile, User,Songs
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Songs)