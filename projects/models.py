from django.db import models

class Project(models.Model):
    projects_name = models.CharField(max_length=128)
    projects_date = models.CharField(max_length=64)
    projects_header = models.CharField(max_length=128, default='')
    projects_summary = models.TextField()

    def __str__(self):
        return self.projects_name