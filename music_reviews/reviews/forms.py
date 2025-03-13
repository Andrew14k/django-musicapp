#form to add new album review
from django import forms
from .models import AlbumReview

class AlbumReviewForm(forms.ModelForm):
    class Meta:
        model = AlbumReview
        fields = ['album_cover', 'album_name', 'artist_name', 'genre', 'favorite_songs', 'rating']
        widgets = {
            'favorite_songs': forms.Textarea(attrs={'rows': 3}),
        }
