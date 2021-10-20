from django.urls import path

from owners.views import OwnerView
from owners.views import DogView

urlpatterns = [
	path('owner', OwnerView.as_view()),
    path('dog', DogView.as_view()),
]