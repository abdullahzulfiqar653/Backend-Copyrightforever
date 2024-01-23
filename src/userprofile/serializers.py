from rest_framework import serializers
from .models import CustomerProfile

class CustomerProfileSerializers(serializers.ModelSerializer):
	class Meta:
		model = CustomerProfile
		fields = ['phone', 'address', 'state', 'postcode']