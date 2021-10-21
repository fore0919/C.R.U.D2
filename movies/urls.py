from django.urls import path

from movies.views import ActorsView
from movies.views import MoviesView


urlpatterns = [
	path('actor', ActorsView.as_view()),
    path('movie', MoviesView.as_view()),
]