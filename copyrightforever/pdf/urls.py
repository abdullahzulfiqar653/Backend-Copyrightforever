from django.urls import path
from .views import (
    VirtualArtWorkFormPrintView,
    LiteraryWorkFormPrintView,
    PerformingArtFormPrintView,
    SerialWorkFormPrintView,
    SoundRecordingFormPrintView,
)

app_name = "pdf"

urlpatterns = [
    path("va/<pk>", VirtualArtWorkFormPrintView.as_view(), name='vapdf'),
    path("tx/<pk>", LiteraryWorkFormPrintView.as_view(), name='txpdf'),
    path("pa/<pk>", PerformingArtFormPrintView.as_view(), name='papdf'),
    path("se/<pk>", SerialWorkFormPrintView.as_view(), name='sepdf'),
    path("sr/<pk>", SoundRecordingFormPrintView.as_view(), name='srpdf'),
]