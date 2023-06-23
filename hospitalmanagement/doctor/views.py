from django.shortcuts import render
from django.views.generic import TemplateView,View

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
    
    