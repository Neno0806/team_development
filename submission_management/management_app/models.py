from django.db import models

class Classroom(models.Model):
    name = models.CharField(max_length=50)