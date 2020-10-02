from django.db import models

# Create your models here.
class Task(models.Model):
    
    STATUSES = (
        ('0', 'Not Started'),
        ('1', 'In Progress'),
        ('2', 'Completed'),
    )
    
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    #status = models.CharField(max_length=1, blank=True, null=True, choices=STATUSES)
    status = models.CharField(max_length=10, blank=True, null=True)
    
    def __str__(self):
        return self.title