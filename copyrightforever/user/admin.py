from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'email',
		'name',
		'is_active',
		'is_staff',
		'is_superuser',
		'last_login'
	]

admin.site.register(User, UserAdmin)