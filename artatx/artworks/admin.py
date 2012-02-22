from django.contrib import admin

from artworks.models import Artwork

class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artist', 'year')

admin.site.register(Artwork, ArtworkAdmin)
