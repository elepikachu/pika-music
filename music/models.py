from django.db import models

# Create your models here.

class Music(models.Model):
    title = models.TextField()
    artist = models.TextField()
    img = models.ImageField()
    audioFile = models.FileField(blank=True, null=True)
    audiolink = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title