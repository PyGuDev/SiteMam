from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from django.db.models import Q
from .models import NewsPost

# Create your views here.


class NewsPage(ListView):
    model = NewsPost
    template_name = "news/index.html"


class SearchListView(ListView):
    model = NewsPost
    template_name = "news/index.html"

    def get_queryset(self):
        queryset = NewsPost.objects.all()
        q = self.request.GET.get("q")
        print(q)
        if q:
            return queryset.filter((Q(title__icontains=q)| Q(text__icontains=q)))

        return queryset


class NewsPageDetail(DeleteView):
    model = NewsPost
    template_name = "news/detail.html"

