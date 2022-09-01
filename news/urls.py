from django.urls import path
from .views import NewsDataList, JobList, index


urlpatterns = [
    path('news-data/', NewsDataList.as_view()),
    path('jobs/', JobList.as_view()),
    path('index/', view=index, name='index')
]