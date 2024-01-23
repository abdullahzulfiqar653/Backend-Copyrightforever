from django.urls import path, include
from .views import GetCustomerProfileView, UpdateCustomerProfileView

urlpatterns = [
	path('profile', GetCustomerProfileView.as_view(),),
	path('update', UpdateCustomerProfileView.as_view()),
]