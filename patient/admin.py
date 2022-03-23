from django.contrib import admin
from django.utils.html import mark_safe
from django_summernote.admin import SummernoteModelAdmin    # to import edit text box and tool
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from import_export.fields import Field


from .models import Add_patient

# Register your models here.

class PatientAdmin(ImportExportActionModelAdmin):
    pass

class AddAdmin(SummernoteModelAdmin, ImportExportModelAdmin):

    search_fields = ['name', 'file_number']
    list_display = ['name', 'file_number', 'idnational']
    list_filter = ['name']
    summernote_fields = ['diagnosis','treatment','note'] # to edit text box and tool

class PatientResource(resources.ModelResource):
    idnational = Field()

    class Meta:
        model = Add_patient

admin.site.register(Add_patient, AddAdmin)
# admin.site.register(Add_patient, PatientAdmin)
# admin.site.register(Add_patient, PatientResource)

