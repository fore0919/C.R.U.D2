from django.urls import path

from owners.views import SampleView
from owners.views import DogView

urlpatterns = [
	path('owner', SampleView.as_view()),
    path('dog', DogView.as_view()),
]