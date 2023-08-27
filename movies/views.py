from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Movie

# Create your views here.
class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'

class MovieCreateView(CreateView):
    model = Movie
    fields = ['title', 'genre', 'release_date', 'rating', 'poster']
    template_name = 'movie_form.html'
    success_url = reverse_lazy('movie_list')

class MovieUpdateView(UpdateView):
    model = Movie
    fields = ['title', 'genre', 'release_date', 'rating', 'poster']
    template_name = 'movie_form.html'
    success_url = reverse_lazy('movie_list')

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')