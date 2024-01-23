from django.contrib import admin
from .models import Transactions

# Register your models here.
class TransactionsAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'user',
		'amount_paid',
		'date_time',
		'transaction_id',
		'payment_order_id',
	]
	readonly_fields = [
		'id',
		'user',
		'amount_paid',
		'date_time',
		'transaction_id',
		'payment_order_id',
	]


admin.site.register(Transactions, TransactionsAdmin)