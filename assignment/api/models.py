from django.db import models

# Create your models here.
class App(models.Model):
    app_name = models.CharField(max_length=100)
    version = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.app_name