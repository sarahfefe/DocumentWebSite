from __future__ import absolute_import, unicode_literals
from celery import Celery, task, share_task
from .models import Confidentiality


@task
def confidentiality_total_docs():
    for k in range(1,Confidentiality.objects.all().count()+1):
        c= Confidentiality.objects.get(pk=k)
        c.total_docs += k*5
        print('in confidentiality task')
        c.save()