from django.db import models


class Project(models.Model):
    ''' Includes Projects fields '''
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "projects"

