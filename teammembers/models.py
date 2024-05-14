from django.db import models

class TeamMembers(models.Model):
    name = models.CharField(max_length = 255)
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'teammembers/')