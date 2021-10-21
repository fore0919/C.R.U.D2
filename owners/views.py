


# Create your views here.

import json

from django.http     import JsonResponse
from django.views    import View

from owners.models import Owner, Dog 

class OwnerView(View):
    def post(self, request): # => CREATE
       
        data     = json.loads(request.body)
        print(data)
        owner    = Owner.objects.create(
            name=data['name'],
            email=data['email'],
            age=data['age']
        )
        return JsonResponse({'MESSAGE':'CREATED'}, status=201)
    
    def get(self, request):
        owners  = Owner.objects.all()
        result = []

        for owner in owners :
            dog_list =[]
            dogs = owner.dog_set.all()

            for dog in dogs:
                dog_info = {
                    'name' : dog.name,
                    'age'  : dog.age,
                }
                dog_list.append(dog_info)

            owner_info = {
                'name'  : owner.name, 
                'email' : owner.email,
                'age'   : owner.age,
                'dog'   : dog_list,
            }

            result.append(owner_info)
        return JsonResponse({'result':result}, status=200)


class DogView(View):
    def post(self, request):
        data    = json.loads(request.body)
        dog     = Dog.objects.create(
            name=data['name'],
            age=data['age'],
            owner=Owner.objects.get(name=data['owner'])
            )
        return JsonResponse({'MESSAGE':'CREATED'}, status=201)

