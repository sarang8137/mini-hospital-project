from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View,FormView,CreateView
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your views here.

class HomeView(TemplateView):
    template_name="index.html"
    
class AboutView(TemplateView):
    template_name="about_us.html"

class ContactView(TemplateView):
    template_name="contact_us.html"
    
class BlogView(TemplateView):
    template_name="blog.html"

class GalleryView(TemplateView):
    template_name="gallery.html"

class ServiceView(TemplateView):
    template_name="services.html"
    
class NavbarView(TemplateView):
    template_name="navbar.html"
class AdminBase(TemplateView):
    template_name="admin_base.html"
class DoctorBase(TemplateView):
    template_name="doctor_base.html"
class DoctorPatient(TemplateView):
    template_name="doctor_patient.html"
class DoctorAppointment(TemplateView):
    template_name="doctor_view_appointment.html"
class DoctorPatientView(TemplateView):
    template_name="doctor_view_patient.html"
class DoctorPatientDischarge(TemplateView):
    template_name="doctor_view_discharge_patient.html"
    
    
    
    
    
    
# class AdminSignUp(View):
#     def get(self,request,*args,**kwargs):
#         form=SignUpForm()
#         return render(request,"signup.html",{"form":form})
#     def post(self,request,*args,**Kwargs):
#         form_data=SignUpForm(data=request.POST)
#         if form_data.is_valid():
#             form_data.save()
#             messages.success(request,"Registration Success")
#             return redirect("home")
#         else:
#             return render(request,"signup.html",{"form":form_data})

# class AdminSignInView(View):
#     def get(self,request,*args,**kwargs):
#         form=SignInForm()
#         return render(request,"signin.html",{"form":form})
#     def post(self,request,*args,**kwargs):
#         form_date=SignInForm(data=request.POST)
#         if form_date.is_valid():
#             uname=form_date.cleaned_data.get("username")
#             pswd=form_date.cleaned_data.get("password")
#             user=authenticate(request,username=uname,password=pswd)
#             # return HttpResponse(user)
#             if user:
#                 login(request,user)  #session created
#                 messages.success(request,"sign in completed")
#                 return redirect("admbase")
#             else:
#                 messages.error(request,"invalid username & password")
#                 return render(request,"signin.html",{"form":form_date})
#         else:
#             return render(request,"signin.html",{"form":form_date})

class DoctorSignUp(View):
    def get(self,request,*args,**kwargs):
        form=DoctorUserForm()
        form2=DoctorForm()
        return render(request,"doctorsignup.html",{"form":form,"form1":form2})
    def post(self,request,*args,**Kwargs):
        form_data=DoctorUserForm(data=request.POST)
        form_data1=DoctorForm(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Registration Success")
            return redirect("home")
        else:
            return render(request,"doctorsignup.html",{"form":form_data,"form1":form_data1})

class DoctorSignInView(View):
    def get(self,request,*args,**kwargs):
        form=SignInForm()
        return render(request,"doctorlogin.html",{"form":form})
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
                return redirect("docbase")
            else:
                messages.error(request,"invalid username & password")
                return render(request,"doctorlogin.html",{"form":form_date})
        else:
            return render(request,"doctorlogin.html",{"form":form_date})

class LgOut(View):
    def get(selg,request,*args,**kwargs):
        logout(request)
        return redirect("nav")