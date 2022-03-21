from dataclasses import fields
from datetime import date
from tkinter import Widget
from django import forms
from .models import Add_patient
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget # to Import edit text box and tool

class CalDate(forms.DateInput):
    input_type = 'date'

class Add_patientForm(forms.ModelForm):
    date            = forms.DateField(widget=CalDate)
    birthdate       = forms.DateField(widget=CalDate)
    next_visit_date = forms.DateField(widget=CalDate)

    diagnosis       = forms.CharField(widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '300px'}}))    # to edit text box and tool
    treatment       = forms.CharField(widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '300px'}}))    # to edit text box and tool
    note            = forms.CharField(widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '300px'}}), label='Dr. Notes')    # to edit text box and tool

    class Meta:
        model       = Add_patient
        fields      = '__all__'
        
class Update_PatientForm(forms.ModelForm):

    date            = forms.DateField(widget=CalDate, label='Today Date')
    age             = forms.CharField(max_length=20, label='Age')
    diagnosis       = forms.CharField(widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '300px'}}), label='Diagnosis')
    wt              = forms.CharField(max_length=20, label='Wt')
    temp            = forms.CharField(max_length=20, label='Temp')
    treatment       = forms.CharField(widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '300px'}}), label='Treatment')
    next_visit_date = forms.DateField(widget=CalDate, label='Next Visit Date')
    note            = forms.CharField(widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '300px'}}), label='Dr.Notes')
    class Meta:
        model = Add_patient
        fields = ('date','age','diagnosis','wt','temp','treatment','next_visit_date','note')
        verbose_name = 'update_pastient'
        verbose_name_plural = 'update_pastients'
