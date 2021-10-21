#from django.shortcuts import render
# Create your views here.
import json

from django.http    import JsonResponse
from django.views   import View

from movies.models  import Actors, Movies

class ActorsView(View):
    def post(self, request) : 
        data    =json.loads(request.body)

        actor   = Actors.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            date_of_birth=['date_of_birth'],
        )
        return JsonResponse({'MESSAGE':'CREATED'}, status=201)

    def get(self, request):
        actors = Actors.objects.all()
        result = []

        for actor in actors :
            movie_list =[]
            movies = actor.movie_set.all()

            for movie in movies:
                movie_list.append({
                    'title' : movie.title
                })
            
            actor_name = actor.first_name + actor.last_name
            
            result.append({
                    'name'  : actor_name,
                    'movies': movie_list,
            })
        return JsonResponse({'result' : result}, status = 200)