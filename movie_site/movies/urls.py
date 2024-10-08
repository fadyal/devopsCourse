from django.urls import path
from . import views
from .views import add_review, movie_detail

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<int:id>/', views.movie_detail, name='movie_detail'),
    path('movies/<int:id>/add_review/', add_review, name='add_review'),
]
