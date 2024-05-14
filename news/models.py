from django.db import models

class News(models.Model):
    title = models.CharField(max_length = 255)
    link = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'news/')