from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomerProfileSerializers
from django.contrib.auth import get_user_model
User = get_user_model()

from .models import CustomerProfile
from forms.models import VirtualArtWorkForm, PerformingArtForm, LiteraryWorkForm, SoundRecordingForm, SerialWorkForm
from forms.serializers import (
	VirtualArtWorkFormUserSerializers,
	PerformingArtFormUserSerializers,
	LiteraryWorkFormUserSerializers,
	SerialWorkFormUserSerializers,
	SoundRecordingFormUserSerializers
)


class GetCustomerProfileView(APIView):
	def get(self, request, format=None):
		try:
			user = self.request.user
			useremail = user.email
			username = user.name
			userid = user.id
			formlist = []
			user = User.objects.get(id=user.id)
			customer_profile = CustomerProfile.objects.get(user=user)
			customer_profile = CustomerProfileSerializers(customer_profile)

			vaforms = VirtualArtWorkForm.objects.filter(user=user).order_by("-submitted_at")
			txforms = LiteraryWorkForm.objects.filter(user=user).order_by("-submitted_at")
			paforms = PerformingArtForm.objects.filter(user=user).order_by("-submitted_at")
			seforms = SerialWorkForm.objects.filter(user=user).order_by("-submitted_at")
			srforms = SoundRecordingForm.objects.filter(user=user).order_by("-submitted_at")
			if vaforms:
				for i in vaforms:
					formlist.append(VirtualArtWorkFormUserSerializers(i).data)
			if txforms:
				for i in txforms:
					formlist.append(LiteraryWorkFormUserSerializers(i).data)
			if paforms:
				for i in paforms:
					formlist.append(PerformingArtFormUserSerializers(i).data)
			if seforms:
				for i in seforms:
					formlist.append(SerialWorkFormUserSerializers(i).data)
			if srforms:
				for i in srforms:
					formlist.append(SoundRecordingFormUserSerializers(i).data)

			return Response({'userid':userid, 'useremail':useremail, 'username':username, 'profile': customer_profile.data, 'userforms':formlist })
		except:
			return Response({'error': 'something went wrong while getting profile'})

class UpdateCustomerProfileView(APIView):
	def put(self, request, format=None):
		try:
			user = self.request.user
			username =user.name
			useremail = user.email

			data = self.request.data
			user = User.objects.get(id=user.id)
			CustomerProfile.objects.filter(user=user).update(phone=data['phone'],
															 address=data['address'],
															 state=data['state'],
															 postcode=data['postcode']
															)
			return Response({'username':username, 'useremail':useremail })
		except:
			return Response({'error':'error while updating'})
