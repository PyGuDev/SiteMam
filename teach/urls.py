from django.urls import path
from .views import TeachPage, download

urlpatterns = [
    path('', TeachPage.as_view(), name="teach"),
    path('file/<pk>', download, name="downloadfile")
]