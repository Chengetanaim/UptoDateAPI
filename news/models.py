from django.db import models

class NewsData(models.Model):
    title = models.CharField(max_length=200)
    website_link = models.URLField(max_length=200)

    class Meta:
        verbose_name_plural = "News Data"

    def __str__(self):
        return self.title

class Job(models.Model):
    company_name = models.CharField(max_length=100)
    description = models.TextField()
    website_link = models.URLField(max_length=200)
    job_type = models.CharField(max_length=50)
    date_posted = models.CharField(max_length=50) 

    def __str__(self):
        return self.company_name   
