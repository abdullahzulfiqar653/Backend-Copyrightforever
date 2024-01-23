from django.shortcuts import render
from django.views.generic import DetailView
from forms.models import (
    VirtualArtWorkForm,
    LiteraryWorkForm,
    PerformingArtForm,
    SerialWorkForm,
    SoundRecordingForm,
)
from django_weasyprint import WeasyTemplateResponseMixin


class VirtualArtWorkFormPrintView(WeasyTemplateResponseMixin, DetailView):
    model = VirtualArtWorkForm
    template_name = 'va.html'
    pdf_attachment = False


class LiteraryWorkFormPrintView(WeasyTemplateResponseMixin, DetailView):
    model = LiteraryWorkForm
    template_name = 'tx.html'
    pdf_attachment = False


class PerformingArtFormPrintView(WeasyTemplateResponseMixin, DetailView):
    model = PerformingArtForm
    template_name = 'pa.html'
    pdf_attachment = False


class SerialWorkFormPrintView(WeasyTemplateResponseMixin, DetailView):
    model = SerialWorkForm
    template_name = 'se.html'
    pdf_attachment = False


class SoundRecordingFormPrintView(WeasyTemplateResponseMixin, DetailView):
    model = SoundRecordingForm
    template_name = 'sr.html'
    pdf_attachment = False
