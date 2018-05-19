from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Reading

# Create your views here.
def home(request):
    return render(request, "home/home.html", {})


def report(request):
    data = Reading.objects.last()

    return TemplateResponse(request, 'index.html', {'data':data})