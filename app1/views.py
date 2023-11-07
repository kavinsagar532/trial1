from django.shortcuts import render,HttpResponse
from django.template import loader
from .models import Book
# Create your views here.

def resume(request):
    template=loader.get_template("resume.html")
    return HttpResponse(template.render())

def table(request):
    a=Book.objects.all()
    return render(request,'table.html',{'a':a})