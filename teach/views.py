from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView
from .models import TeachFile
# Create your views here.

def download(request, pk):
    obj = TeachFile.objects.get(pk=pk)
    return redirect(obj.file.url)

class TeachPage(ListView):
    model = TeachFile
    template_name = "teach/index.html"