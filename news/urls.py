from django.urls import path
from .views import NewsDataList, JobList


urlpatterns = [
    path('news-data/', NewsDataList.as_view()),
    path('jobs/', JobList.as_view()),
]