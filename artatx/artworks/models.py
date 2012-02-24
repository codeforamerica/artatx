from django.db import models

class Artwork(models.Model):
    level = models.SmallIntegerField()
    work_num = models.CharField(max_length=10)
    artist = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    year = models.SmallIntegerField()
    medium = models.CharField(max_length=255)
    credit = models.CharField(max_length=255)
    website = models.URLField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.title
