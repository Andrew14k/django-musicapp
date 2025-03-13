from django.shortcuts import render, redirect
from .models import AlbumReview
from .forms import AlbumReviewForm

# Create view to handle requests - displays the reviews

# View to display all reviews
def review_list(request):
    reviews = AlbumReview.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

# View to add a new review
def add_review(request):
    if request.method == 'POST':
        form = AlbumReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = AlbumReviewForm()
    return render(request, 'reviews/add_review.html', {'form': form})