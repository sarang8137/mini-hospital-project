from .forms import *
from .views import *
from django.urls import path

urlpatterns = [
    path('signup',AdminSignUp.as_view(),name='signup'),
    path('signin',AdminSignInView.as_view(),name="signin"),
    path('docsignup',DoctorSignUp.as_view(),name='docsignup'),
    path('docsignin',DoctorSignInView.as_view(),name="docsignin"),
    # path('logout',LgOut.as_view(),name='logout'),
]