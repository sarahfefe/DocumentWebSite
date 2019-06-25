from __future__ import absolute_import, unicode_literals
from django.apps import apps
from django.conf import settings
import os
 
from celery import Celery
 
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dathenaWebSite.settings')
 
 
app = Celery('dathenaWebSite')
 
# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object(settings, namespace='CELERY')
app = Celery('tasks', broker='redis://localhost:6379/0')
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
    
    