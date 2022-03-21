from django.shortcuts import render, get_object_or_404, redirect
from patient.models import Add_patient
from .forms import Add_patientForm, Update_PatientForm
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def home(request):
    return render(request, 'index.html')

# ---------------------------------
# Add Patient to DB From HTML File and this old methods
# ---------------------------------
# def add_patient(request):
          
#     file_number         = request.POST.get('file_number')
#     name                = request.POST.get('name')
#     birthdate           = request.POST.get('birthdate')
#     gender              = request.POST.get('gender')
#     adderss             = request.POST.get('adderss')
#     mobile_no           = request.POST.get('mobile_no')
#     diagnosis           = request.POST.get('diagnosis')
#     age                 = request.POST.get('age')
#     next_visit_date     = request.POST.get('next_visit_date')
#     treatment           = request.POST.get('treatment')
#     temp                = request.POST.get('temp')
#     wt                  = request.POST.get('wt')
#     note                = request.POST.get('note')
    
#     dataform = Add_patient(
#         file_number=file_number,
#         name=name,
#         birthdate=birthdate,
#         gender=gender,
#         adderss=adderss,
#         mobile_no=mobile_no,
#         diagnosis=diagnosis,
#         age=age,
#         next_visit_date=next_visit_date,
#         treatment=treatment,
#         wt=wt,
#         note=note,
#         temp=temp)
    
#     if request.method == 'POST':
#         dataform.save()
#     return render(request,'add-patient.html')

# ---------------------------------
# Add Patient to DB From HTML File and this file come from forms
# ---------------------------------

def add_patient(request): #def add_patient in urls
    if request.method == 'POST': #POST in form add_patient in add_patient html
        formtohtml = Add_patientForm(request.POST) # add_patientForm come from forms.py
        if formtohtml.is_valid():
            formtohtml.save() # to save data in forms
            messages.success(request, 'Add Patient Successful.')
    return render(request,'add_patient.html',{'formtohtml':Add_patientForm}) # Add_patientForm From forms.py 
# ---------------------------------
#  END Add Patient to DB Code
# ---------------------------------
# ---------------------------------
# Search From HTML File To Get Results in another files
# ---------------------------------
def result(request):
   
    queryfromhtml=request.GET['q'] # queryfromhtml to def request q and q come from html search field
    if queryfromhtml:
        # query=Add_patient.objects.filter(name__iexact=queryfromhtml)
        multple_q = Q(Q(name__iexact=queryfromhtml) | Q(file_number__iexact=queryfromhtml)) # def multple_q and Q to allow search 2 fields
        query = Add_patient.objects.filter(multple_q) # to do my search multple
        context={
            'regdr1':query # regdr to use in HTML files query my varibal in above 
        }
    else:
        context={}
    return render(request,'patient/result.html',context)
# ---------------------------------
#  END Search Results Code
# ---------------------------------


# ---------------------------------
# Search From HTML File To Get Results in another files
# ---------------------------------
# def edit_patient(request):
#     patient = get_object_or_404(Add_patient)
#     queryfromhtml=request.GET['q'] # queryfromhtml to def request q and q come from html search field
#     if queryfromhtml:
#         # query=Add_patient.objects.filter(name__iexact=queryfromhtml)
#         # multple_q = Q(Q(name__iexact=queryfromhtml) | Q(file_number__iexact=queryfromhtml)) # def multple_q and Q to allow search 2 fields
#         query = Add_patient.objects.filter(instance=patient) # to do my search multple
#         context={
#             'regdr':query # regdr to use in HTML files query my varibal in above 
#         }
#     else:
#         context={}
#     return render(request,'edit_patient.html',context)
# ---------------------------------
#  END Search Results Code
# ---------------------------------


# ---------------------------------
# Add Patient to DB From HTML File and this file come from forms
# ---------------------------------

def edit_patient(request, id): #def edit_patient in urls
    edit = get_object_or_404(Add_patient, idnational=id)
    if request.method == 'POST': #POST in form edit_patient in edit_patient html
        formtohtml = Update_PatientForm(request.POST, instance=edit) # edit_patient come from forms.py
        if formtohtml.is_valid():
            formtohtml.save() # to save data in forms
            messages.success(request, 'Update Patient Successful.')
            
    else:
        formtohtml= Update_PatientForm(instance=edit)
    return render(request,'patient/edit.html',{'updatehtml':formtohtml}) # edit_patient From forms.py 
# ---------------------------------
#  END Add Patient to DB Code
# ---------------------------------