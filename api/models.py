from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(("title_2"),max_length=50)
    description = models.TextField(null=False)