# Generated by Django 3.1.4 on 2021-01-02 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='projects_header',
            field=models.CharField(default='', max_length=128),
        ),
    ]
