from __future__ import absolute_import, unicode_literals
from celery import Celery, task, share_task
from .models import DataType



@task
def docType_total_docs():
    for k in range(1,DataType.objects.all().count()+1):
        dt= DataType.objects.get(pk=k)
        dt.total_docs += k*5
        dt.save()

    