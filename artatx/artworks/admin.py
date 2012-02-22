from django.contrib import admin

from artworks.models import ArtWork

class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artist', 'year')

admin.site.register(ArtWork, ArtworkAdmin)
