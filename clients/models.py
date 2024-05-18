from django.db import models

class Clients(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'clients/')

    def __str__(self):
        return self.name