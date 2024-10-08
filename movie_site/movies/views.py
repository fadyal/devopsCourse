from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})

# def movie_detail(request, id):
#     movie = get_object_or_404(Movie, id=id)
#     return render(request, 'movie_detail.html', {'movie': movie})

def movie_detail(request, id):
    movie = get_object_or_404(Movie, pk=id)

    # If you have a related field like reviews or actors
    reviews = movie.reviews.all()  # Fetch all related reviews

    return render(request, 'movie_detail.html', {'movie': movie, 'reviews': reviews})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review
from .forms import ReviewForm


def add_review(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.reviewer = request.user
            review.save()
            return redirect('movie_detail', id=movie.id)
    else:
        form = ReviewForm()

    return redirect('movie_detail', id=movie.id)
