from django import forms
from django.contrib.auth.models import User
from patient.models import *
from django.contrib.auth.forms import UserCreationForm
from .models import *

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]

class SignInForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Username','class':'form-control'}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control'}))




#for doctor related form
class DoctorUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']
        widgets = {
            "username":forms.TextInput(attrs={'placeholder':'username','class':'form-control'}),
            'password1': forms.PasswordInput(attrs={'placeholder':'Enter password','class':'form-control'}),
            'password2': forms.PasswordInput(attrs={'placeholder':'Enter password','class':'form-control'}),
        }
class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields="__all__"

# class DoctorUserForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['username','password']
#         widgets = {
#         'password': forms.PasswordInput()
#         }
# class DoctorForm(forms.ModelForm):
#     class Meta:
#         model=Doctor
#         fields="__all__"




#for patient related form
class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class PatientForm(forms.ModelForm):
    # assignedDoctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Name and Department", to_field_name="user_id")
    class Meta:
        model=Patient
        fields=['Name','address','mobile','status','symptoms','profile_pic']



class AppointmentForm(forms.ModelForm):
    # doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    # patientId=forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),empty_label="Patient Name and Symptoms", to_field_name="user_id")
    class Meta:
        model=Appointment
        fields=['patientName','doctorName','description','status']


class PatientAppointmentForm(forms.ModelForm):
    # doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    class Meta:
        model=Appointment
        fields=['description','status']


