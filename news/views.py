from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import NewsPost
# Create your views here.


class NewsPage(ListView):
    model = NewsPost
    template_name = "news/index.html"

class NewsPageDetail(DeleteView):
    model = NewsPost
    template_name = "news/detail.html"