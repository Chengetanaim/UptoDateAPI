from django.shortcuts import render
from .serializers import NewsDataSerializer, JobSerializer
from .models import NewsData, Job
from rest_framework import generics
from .jobs import job_links, company_names, descriptions, job_types, dates_added
from .newsdata import titles, website_links
import itertools

def addnews():
    for (title1, website_link1) in zip(titles, website_links):
        new = NewsData(title=title1, website_link=website_link1)
        new.save()




def addjob():
    for (job_link, company_name, description, job_type, date_posted) in zip(job_links, company_names, descriptions, job_types, dates_added):
        new_job = Job(company_name=company_name, description=description, website_link=job_link, job_type=job_type, date_posted=date_posted)
        new_job.save()

        
addnews()
addjob()



class NewsDataList(generics.ListAPIView):
    queryset = NewsData.objects.order_by('-id')
    serializer_class = NewsDataSerializer


class JobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


