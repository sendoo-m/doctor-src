from unicodedata import name
from django.db import models


# Create your models here.
GENDER = (
    ('Male', 'Male'),
    ('Female','Female')
)
class Add_patient(models.Model):
    idnational      = models.IntegerField(primary_key=True)
    file_number     = models.CharField(max_length=30, verbose_name='File Number',null=True, blank=False)
    name            = models.CharField(max_length=120, verbose_name='Name', null=True, blank=True)
    birthdate       = models.DateField(verbose_name='Birth Date')
    date            = models.DateField(verbose_name='Today Date')
    age             = models.CharField(max_length=20, verbose_name='Age' ,null=True, blank=True)
    gender          = models.CharField(max_length=10, choices=(GENDER), default=('Male'))
    adderss         = models.CharField(max_length=250, verbose_name='Address' , null=True, blank=True)
    mobile_no       = models.CharField(max_length=30, verbose_name='Phone Number', null=True, blank=True)
    diagnosis       = models.TextField(max_length=1200, verbose_name='Diagnosis', null=True, blank=True)
    wt              = models.CharField(max_length=20, verbose_name='Wt' ,null=True, blank=True)
    temp            = models.CharField(max_length=20, verbose_name='Temp', null=True, blank=True)
    treatment       = models.TextField(max_length=1200, verbose_name='Treatment', null=True, blank=True)
    next_visit_date = models.DateField(verbose_name='Next Visit Date', null=True, blank=True)
    note            = models.TextField(max_length=1200, verbose_name='Dr. Notes', null=True, blank=True)

    def __str__(self):
        return self.name or ''
        
    class Meta:
        verbose_name = "registration"
        verbose_name_plural = "registration"


class Doctor(models.Model):
    name            = models.CharField(max_length=50, verbose_name='Doctor`s name', null=True, blank=True)
    specialty       = models.CharField(max_length=50, verbose_name='Specialty', null=True, blank=True)
    mobile_number   = models.CharField(max_length=11, verbose_name='Mobile Number', null=True, blank=True)
    address         = models.CharField(max_length=500, verbose_name='Address', null=True, blank=True)
    

    def __str__(self):
        return self.name or ''
        
    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctor"


# class Patient(models.Model):
#     date            = models.DateField(verbose_name='Today Date')
#     age             = models.CharField(max_length=20, verbose_name='Age' ,null=True, blank=True)
#     diagnosis       = models.TextField(max_length=1200, verbose_name='Diagnosis', null=True, blank=True)
#     wt              = models.CharField(max_length=20, verbose_name='Wt' ,null=True, blank=True)
#     temp            = models.CharField(max_length=20, verbose_name='Temp', null=True, blank=True)
#     treatment       = models.TextField(max_length=1200, verbose_name='Treatment', null=True, blank=True)
#     note            = models.TextField(max_length=1200, verbose_name='Dr. Notes', null=True, blank=True)

    
#     def __str__(self):
#         return self.name or ''
             
#     class Meta:
#         verbose_name = "patient"
#         verbose_name_plural = "patient"

class Cashf(models.Model):
    doctor          = models.ForeignKey(Doctor, verbose_name='Doctor Cashf', on_delete=models.CASCADE)
    # patient         = models.ForeignKey(Patient, verbose_name='Patient Cashf', on_delete=models.CASCADE)
    detection_cost  = models.DecimalField(max_digits=6,decimal_places=2, verbose_name='Detection Cost')
    date            = models.DateField(verbose_name='date Cashf')
    next_visit_date = models.DateField(verbose_name='Next Visit Date')

    # def __str__(self):
    #      return self.doctor or ''
             
    class Meta:
        verbose_name = "Cashf"
        verbose_name_plural = "Cashf"

class Rosheta(models.Model):
    doctor          = models.ForeignKey(Doctor, verbose_name='Doctor`s Rosheta', on_delete=models.CASCADE)
    # patient         = models.ForeignKey(Patient, verbose_name='Patient Rosheta', on_delete=models.CASCADE)
    diagnosis       = models.CharField(max_length=1200, verbose_name='Diagnosis', null=True, blank=True)
    treatment       = models.CharField(max_length=1200, verbose_name='Treatment', null=True, blank=True)
    note            = models.CharField(max_length=1200, verbose_name='Dr. Notes', null=True, blank=True)

    def __str__(self):
        return self.diagnosis or ''
             
    class Meta:
        verbose_name = "Roshita"
        verbose_name_plural = "Roshita"
