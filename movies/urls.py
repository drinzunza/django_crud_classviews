from django.urls import path
from .views import MovieListView, MovieDetailView
from .views import MovieCreateView, MovieUpdateView, MovieDeleteView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('new/', MovieCreateView.as_view(), name='movie_new'),
    path('<int:pk>/edit/', MovieUpdateView.as_view(), name='movie_edit'),
    path('<int:pk>/delete/', MovieDeleteView.as_view(), name='movie_delete'),
]