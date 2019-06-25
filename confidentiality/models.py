from django.db import models

# Create your models here.

class Confidentiality(models.Model):
    name=models.CharField(max_length=20)
    total_docs=models.IntegerField()
    def __str__(self):
        return self.name
