from django.db import models

# Create your models here.
class Language(models.Model):
    name=models.CharField(max_length=20)
    short_name=models.CharField(max_length=5,unique=True)
    total_docs=models.IntegerField()    
    def __str__(self):
        return self.name