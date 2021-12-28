from django.urls import path, include


urlpatterns = [
	path('user/', include('userprofile.api')),
	path('add/',  include('forms.api')),
	path('pdf/',  include('pdf.urls')),
	# path('vaform/',  include('vaform.api')),
	# path('txform/',  include('txform.api')),
	# path('paform/',  include('paform.api')),
	# path('seform/',  include('seform.api')),
	# path('srform/',  include('srform.api')),
]