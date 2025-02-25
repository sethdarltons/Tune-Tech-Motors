from pickletools import read_uint1
from django.shortcuts import render
from django.views import View 
# Create your views here.

def home_page(request):
    return render(request,"tutor.html")

def about_page(request):
    return render(request,'about.html')
def serv_page(request):
    return render(request,'serv.html')
def blog_page(request):
    return render(request,'blog.html')
def contract(request):
    return render(request,'contact.html')