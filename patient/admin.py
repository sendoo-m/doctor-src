from django.contrib import admin
from django.utils.html import mark_safe
from django_summernote.admin import SummernoteModelAdmin    # to import edit text box and tool

from .models import Add_patient

# Register your models here.

class AddAdmin(SummernoteModelAdmin):

    search_fields = ['name', 'file_number']
    list_display = ['name', 'file_number', 'idnational']
    list_filter = ['name']
    summernote_fields = ['diagnosis','treatment','note'] # to edit text box and tool


admin.site.register(Add_patient,AddAdmin)

