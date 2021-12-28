from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from userprofile.models import CustomerProfile
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
	class Meta(UserCreateSerializer.Meta):
		model = User
		fields = ['id', 'email', 'name', 'password', 'is_superuser']

		def create(self, validated_data):
			print(validated_data)
			instance = super(UserCreateSerializer, self).create(validated_data)
			CustomerProfile.objects.create(user=instance)
			return instance