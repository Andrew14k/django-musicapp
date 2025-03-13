from django.contrib import admin
from .models import AlbumReview
from django.utils.html import format_html

# Register your album review in the django admin site.
class AlbumReviewAdmin(admin.ModelAdmin):
    list_display = ('album_name', 'artist_name', 'genre', 'rating', 'album_cover_thumb', 'date_added')

    # Method to show a thumbnail of the album cover in the admin list view
    def album_cover_thumb(self, obj):
        if obj.album_cover:
            return format_html('<img src="{}" width="50" height="50"/>', obj.album_cover.url)
        return "-"
    album_cover_thumb.short_description = 'Album Cover'

    search_fields = ('album_name', 'artist_name', 'genre')
    list_filter = ('genre', 'rating')

admin.site.register(AlbumReview, AlbumReviewAdmin)