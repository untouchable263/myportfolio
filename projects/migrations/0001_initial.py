# Generated by Django 3.1.4 on 2021-01-02 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projects_name', models.CharField(max_length=128)),
                ('projects_date', models.CharField(max_length=64)),
                ('projects_summary', models.TextField()),
            ],
        ),
    ]
