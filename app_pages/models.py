from django.db import models

class EmailForm(models.Model):
    to = models.EmailField()
    title = models.CharField(max_length=255)
    message = models.TextField()