from django.db import models

# Create your models here.
class Visitor(models.Model):
    
    ip_address = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    country_full_name = models.CharField(max_length=50, null=True, blank=True)
    region = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    latitude = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    longitude = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    visit_date = models.DateField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        
        return self.country + ', ' + self.region + ', ' + self.city