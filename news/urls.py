from django.urls import path
from .views import NewsPage, NewsPageDetail, SearchListView

urlpatterns = [
    path('', NewsPage.as_view(), name="news"),
    path('<pk>/', NewsPageDetail.as_view(), name="newsdetail"),
    path('article_search', SearchListView.as_view(), name="article_search")
]
