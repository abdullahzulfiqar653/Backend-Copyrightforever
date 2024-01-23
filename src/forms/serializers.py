from rest_framework import serializers
from .models import VirtualArtWorkForm, PerformingArtForm, LiteraryWorkForm, SoundRecordingForm, SerialWorkForm

class VirtualArtWorkFormSerializers(serializers.ModelSerializer):
	# user_id = serializers.CharField(source='id')
	class Meta:
		model = VirtualArtWorkForm
		fields = '__all__'


class VirtualArtWorkFormUserSerializers(serializers.ModelSerializer):
	# user_id = serializers.CharField(source='id')
	class Meta:
		model = VirtualArtWorkForm
		fields = [
			'id',
			'paid',
			'submitted_at',
			'form_name'
		]

#LiterraryWork
class LiteraryWorkFormSerializers(serializers.ModelSerializer):
	class Meta:
		model = LiteraryWorkForm
		fields = '__all__'


class LiteraryWorkFormUserSerializers(serializers.ModelSerializer):
	class Meta:
		model = LiteraryWorkForm
		fields = [
			'id',
			'paid',
			'submitted_at',
			'form_name'
		]


#PerformingArt
class PerformingArtFormUserSerializers(serializers.ModelSerializer):
	class Meta:
		model = PerformingArtForm
		fields = [
			'id',
			'paid',
			'submitted_at',
			'form_name'
		]


class PerformingArtFormSerializers(serializers.ModelSerializer):
	class Meta:
		model = PerformingArtForm
		fields = '__all__'


#SoundRecording
class SoundRecordingFormUserSerializers(serializers.ModelSerializer):
	class Meta:
		model = SoundRecordingForm
		fields = [
			'id',
			'paid',
			'submitted_at',
			'form_name'
		]


class SoundRecordingFormSerializers(serializers.ModelSerializer):
	class Meta:
		model = SoundRecordingForm
		fields = '__all__'


#SerialWork
class SerialWorkFormUserSerializers(serializers.ModelSerializer):
	class Meta:
		model = SerialWorkForm
		fields = [
			'id',
			'paid',
			'submitted_at',
			'form_name'
		]


class SerialWorkFormSerializers(serializers.ModelSerializer):
	class Meta:
		model = SerialWorkForm
		fields = '__all__'
