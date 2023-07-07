from django.shortcuts import render
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View,FormView,CreateView
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from doctor.forms import *
from doctor.models import Appointment


# Create your views here.
class PatientBase(TemplateView):
    template_name="patient_base.html"
    
class PatientAppo(TemplateView):
    template_name="patient_book_appointment.html"

class PatientDischarge(TemplateView):
    template_name="patient_discharge.html"
    




class PatientSignUp(View):
    def get(self,request,*args,**kwargs):
        form=PatientUserForm()
        form2=PatientForm()
        return render(request,"patientsignup.html",{"form":form,"form1":form2})
    def post(self,request,*args,**Kwargs):
        form_data=PatientUserForm(data=request.POST)
        form_data1=PatientForm(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Registration Success")
            return redirect("home")
        else:
            return render(request,"patientsignup.html",{"form":form_data,"form1":form_data1})

class PatientSignInView(View):
    def get(self,request,*args,**kwargs):
        form=SignInForm()
        return render(request,"patientlogin.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form_date=SignInForm(data=request.POST)
        if form_date.is_valid():
            uname=form_date.cleaned_data.get("username")
            pswd=form_date.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pswd)
            # return HttpResponse(user)
            if user:
                login(request,user)  #session created
                messages.success(request,"sign in completed")
                return redirect("patbase")
            else:
                messages.error(request,"invalid username & password")
                return render(request,"patientlogin.html",{"form":form_date})
        else:
            return render(request,"patientlogin.html",{"form":form_date})

class PatientAppointment(View):
    def get(self,request,*args,**kwargs):
        form=AppointmentForm()
        return render(request,"patient_book_appointment.html",{"form":form})
    def post(self,request,*args,**Kwargs):
        form_data=AppointmentForm(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Registration Success")
            return redirect("home")
        else:
            return render(request,"patientsignup.html",{"form":form_data})
