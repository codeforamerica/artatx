from django.db import models

class ArtWork(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    year = models.SmallIntegerField()
    website = models.URLField(max_length=255)

    def __unicode__(self):
        return self.title
