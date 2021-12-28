from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Transactions(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	amount_paid = models.CharField(max_length=5)
	date_time = models.DateTimeField()
	transaction_id = models.CharField(max_length=256)
	payment_order_id = models.CharField(max_length=256)

	class Meta:
		verbose_name = 'Transactions History'