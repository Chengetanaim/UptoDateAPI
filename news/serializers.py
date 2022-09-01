from rest_framework import serializers
from .models import NewsData, Job


class NewsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsData
        fields = ('id', 'title', 'website_link')

    
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'company_name', 'description', 'website_link', 'job_type', 'date_posted')