# Generated by Django 2.2.1 on 2019-05-16 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='short_name',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]
