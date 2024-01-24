from django.db import models


# Create your models here.
class DashboardData(models.Model):
    intensity = models.IntegerField()
    likelihood = models.IntegerField()
    relevance = models.IntegerField()
    year = models.IntegerField()
    country = models.CharField(max_length=255)
    topics = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

     
    
    def __str__(self):
        return f"{self.year} - {self.country} - {self.topics} - {self.intensity} - {self.likelihood} - {self.relevance} - {self.region} - {self.city}"