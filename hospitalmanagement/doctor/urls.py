from .forms import *
from .views import *
from django.urls import path

urlpatterns = [
    # path('signup',AdminSignUp.as_view(),name='signup'),
    # path('signin',AdminSignInView.as_view(),name="signin"),
    path('docsignup',DoctorSignUp.as_view(),name='docsignup'),
    path('docsignin',DoctorSignInView.as_view(),name="docsignin"),
    path('admbase',AdminBase.as_view(),name="admbase"),
    path('docbase',DoctorBase.as_view(),name="docbase"),
    path('docpat',DoctorPatient.as_view(),name="docpat"),
    path('docpatappo',DoctorAppointment.as_view(),name="docpatappo"),
    path('approve',ApproveAppointment.as_view(),name="approve"),
    path('docpatview',DoctorPatientView.as_view(),name="docpatview"),
    path('deleteappo/<int:id>',DeleteAppointment.as_view(),name="deleteappo"),
    path('confirm/<int:id>',ConfirmAppointment.as_view(),name="confirm"),
]