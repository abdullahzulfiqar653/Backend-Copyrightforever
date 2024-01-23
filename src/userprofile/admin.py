from django.contrib import admin
from .models import CustomerProfile

# Register your models here.
class CustomerProfileAdmin(admin.ModelAdmin):
	list_display = [
		'user',
		'phone',
		'state',
		'postcode'
	]
	readonly_fields = [
		'user',
		'phone',
		'state',
		'postcode',
		'address',
	]
admin.site.register(CustomerProfile, CustomerProfileAdmin)