from django.db import models


class project(models.Model):
    title = models.CharField(max_length=150)
    details = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    id = models.IntegerField(primary_key=True)
    owner = models.CharField(max_length=100)
    # image

    def __str__(self):
        return self.title
