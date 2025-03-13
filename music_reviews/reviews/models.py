from django.db import models

# Create your models here.
#Stores album details
class AlbumReview(models.Model):
    album_cover = models.ImageField(upload_to='album_covers/', blank=True, null=True)  # Path where images are stored
    album_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    favorite_songs = models.TextField()  # Store favorite songs as a list or text
    rating = models.PositiveIntegerField()  # Rating from 1-10
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.album_name} by {self.artist_name}'