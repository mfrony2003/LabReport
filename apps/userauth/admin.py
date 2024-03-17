from django.contrib import admin

from apps.userauth.models import User,Role



# Register your models here.
admin.site.register(User)
admin.site.register(Role)