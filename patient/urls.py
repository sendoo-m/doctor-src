from django.urls import path, include
from .views import result, add_patient, home, edit_patient
from django.conf import settings
from django.conf.urls.static import static

app_name = 'patient'
urlpatterns = [
    path('', home, name='home'),
    path('add_patient', add_patient, name='add_patient'),
    path('patient/result', result, name='result'),
    # path('patient/edit', edit_patient, name='edit'),
    path('<int:id>/edit', edit_patient, name='edit'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
