# Generated by Django 2.2.1 on 2019-05-17 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('datafile', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]