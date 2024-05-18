from django.db import models

class Gallery(models.Model):
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'gallery/')

    def __str__(self):
        return self.description