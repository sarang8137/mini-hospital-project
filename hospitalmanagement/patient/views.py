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
from patient.models import Appointment


# Create your views here.
class PatientBase(TemplateView):
    template_name="patient_base.html"
    



class PatientSignUp(View):
    def get(self,request,*args,**kwargs):
        #form=PatientUserForm()
        form1=PatientForm()
        return render(request,"patientsignup.html",{"form1":form1})
    def post(self,request,*args,**Kwargs):
        #form_data=PatientUserForm(data=request.POST)
        form_data1=PatientForm(data=request.POST)
        if form_data1.is_valid():
           # form_data.save()
            form_data1.save()
            messages.success(request,"Registration Success")
            return redirect("home")
        else:
            return render(request,"patientsignup.html",{"form1":form_data1})

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


class PatientAppo(TemplateView):
    template_name="patient_book_appointment.html"
    def get(self,request,*args,**kwargs):
        form=AppointmentForm()
        doc=Doctor.objects.all()
        return render(request,"patient_book_appointment.html",{"form":form,"doc":doc})
    def post(self,request):
        # patid=request.POST.get("patname")
        # docid=request.POST.get("patname")
        patname=request.POST.get("patname")
        docname=request.POST.get("docname")
        appdate=request.POST.get("appdate")
        desc=request.POST.get("desc")
        sts=request.POST.get("sts")

        Appointment.objects.create(
            # patient=patid,
            # doctor=docid,
            patientName=patname,
            doctorName=docname,
            appointmentDate=appdate,
            description=desc,
            status=sts
        )
        return render(request,"index.html")
    
class ViewAppointment(View):
    def get(self,request,*args,**kwargs):
            data=Appointment.objects.all()
            return render(request,"patient_view_appointment.html",{"data":data})

