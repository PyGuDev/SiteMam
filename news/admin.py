from django.contrib import admin
from .models import NewsPost


@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'avilable')
    list_filter = ('avilable',)


