from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .serializers import VirtualArtWorkFormSerializers, PerformingArtFormSerializers, LiteraryWorkFormSerializers, SerialWorkFormSerializers, SoundRecordingFormSerializers
from rest_framework.response import Response
from .models import VirtualArtWorkForm, PerformingArtForm, LiteraryWorkForm, SoundRecordingForm, SerialWorkForm
from transaction.models import Transactions


class VaFormCreateApiView(CreateAPIView):
	serializer_class = VirtualArtWorkFormSerializers
	def perform_create(self, serializer):
		try:
			return super(VaFormCreateApiView, self).perform_create(serializer=serializer)
		except Exception as e:
			return Response({"error":"error while submitting form "})


class TxFormCreateApiView(CreateAPIView):
	serializer_class = LiteraryWorkFormSerializers
	def perform_create(self, serializer):
		try:
			return super(TxFormCreateApiView, self).perform_create(serializer=serializer)
		except Exception as e:
			print(e)
			return Response({"error": "error while submitting form "})


class PaFormCreateApiView(CreateAPIView):
	serializer_class = PerformingArtFormSerializers
	def perform_create(self, serializer):
		try:
			return super(PaFormCreateApiView, self).perform_create(serializer=serializer)
		except Exception as e:
			print(e)
			return Response({"error": "error while submitting form "})


class SeFormCreateApiView(CreateAPIView):
	serializer_class = SerialWorkFormSerializers
	def perform_create(self, serializer):
		try:
			return super(SeFormCreateApiView, self).perform_create(serializer=serializer)
		except Exception as e:
			print(e)
			return Response({"error": "error while submitting form "})


class SrFormCreateApiView(CreateAPIView):
	serializer_class = SoundRecordingFormSerializers
	def perform_create(self, serializer):
		try:
			return super(SrFormCreateApiView, self).perform_create(serializer=serializer)
		except Exception as e:
			print(e)
			return Response({"error": "error while submitting form "})


class VaPaymentApiVIEW(RetrieveAPIView):
	def post(self, request, format=None):
		try:
			user = self.request.user
			data = self.request.data
			print(data)
			if data['formName'] == 'VA VitualArts Work':
				form = VirtualArtWorkForm.objects.get(id=data['form_id'])
				form.paid = True
				form.save()
			elif data['formName'] == 'TX Literary Works':
				form = LiteraryWorkForm.objects.get(id=data['form_id'])
				form.paid = True
				form.save()
			elif data['formName'] == 'PA Performing Arts':
				form = PerformingArtForm.objects.get(id=data['form_id'])
				form.paid = True
				form.save()
			elif data['formName'] == 'SE Serial Works':
				form = SerialWorkForm.objects.get(id=data['form_id'])
				form.paid = True
				form.save()
			elif data['formName'] == 'SR Sound Recording':
				form = SoundRecordingForm.objects.get(id=data['form_id'])
				form.paid = True
				form.save()

			Transactions.objects.create(
				user=user,
				amount_paid=data['amount_paid'],
				date_time = data['date_time'],
				transaction_id = data['transaction_id'],
				payment_order_id = data['payment_order_id']
			)

			return Response({'success' : 'Payment done successfuly'})
		except Exception as e:
			return Response({'error': 'Error Occur! Contaact to site '})


# def generate_pdf( template, dict = {}):
# 	print(dict)
# 	html = template.render(dict)
# 	print(template)
# 	result = BytesIO()
# 	print(dict)
# 	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
# 	print()
# 	if not pdf.err:
# 		print("hehehehe")
# 		return HttpResponse(result.getvalue(), content_type='application/pdf')
# 	return None

