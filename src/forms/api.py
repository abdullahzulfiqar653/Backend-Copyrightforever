from django.urls import path
from .views import (
	PaFormCreateApiView,
	VaFormCreateApiView,
	TxFormCreateApiView,
	SeFormCreateApiView,
	SrFormCreateApiView,
	VaPaymentApiVIEW,
)

urlpatterns = [
	path('vaform', VaFormCreateApiView.as_view(),),
	path('txform', TxFormCreateApiView.as_view(),),
	path('paform', PaFormCreateApiView.as_view(),),
	path('seform', SeFormCreateApiView.as_view(),),
	path('srform', SrFormCreateApiView.as_view(),),
	path('payment', VaPaymentApiVIEW.as_view()),
]