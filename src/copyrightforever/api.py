from django.urls import path, include


urlpatterns = [
	path('user/', include('userprofile.api')),
	path('add/',  include('forms.api')),
	path('pdf/',  include('pdf.urls'))
]
