from doctor.forms import *
from .views import *
from django.urls import path

urlpatterns = [
    path('patsignup',PatientSignUp.as_view(),name='patsignup'),
    path('patsignin',PatientSignInView.as_view(),name="patsignin"),
    path('patbase',PatientBase.as_view(),name="patbase"),
    path('patappo',PatientAppo.as_view(),name="patappo"),
    path('viewappopat',ViewAppointment.as_view(),name="viewappopat"),
    

]