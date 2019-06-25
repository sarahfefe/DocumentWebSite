from __future__ import absolute_import, unicode_literals
from celery import  Celery, task, share_task
from .models import Language



@task
def language_total_docs():
    for k in range(1,Language.objects.all().count()+1):
        lg= Language.objects.get(pk=k)
        lg.total_docs += k*2
        lg.save()