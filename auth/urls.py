from django.urls import path, include


urlpatterns = [
    path('accounts/', include('django.contrib.registration.urls')),
]