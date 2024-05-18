from django.db import models

class LegalServices(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'legalservices/')

    def __str__(self):
        return self.title