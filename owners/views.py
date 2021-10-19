
from django.shortcuts import render

# Create your views here.

import json

from django.http     import JsonResponse
from django.views    import View

from owners.models import Owner, Dog 

class SampleView(View):
    def post(self, request): # => CREATE
        #backend
        # 1. models.py -> 테이블 구조 만들기(column) => CRUD1
        # 2. view.py -> 데이터 입력 => CRUD2 ()
            #2-1. 데이터? -> http 통신-> request.body -> json를 변수에 담기
            #2-2. 데이터를 가공 => json 형태(딕셔너리)에서 key를 이용해서 value를 찾기
            #2-3. value를 데이터베이스 저장
            #2-4. value를 저장할 때는 key값과 table의 column이 일치하는 지 보고 다르면 수정해서 로직짜기
        data     = json.loads(request.body)
        print(data)
        owner    = Owner.objects.create(
            name=data['name'],
            email=data['email'],
            age=data['age']
        )
        return JsonResponse({'MESSAGE':'CREATED'}, status=201)
    
    def get(self, request):
        owner   = Owner.objects.all()
        result = []

        for owner in owner :
            dog_list =[]
            dogs = Owner.dog_set.all()

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
        return JsonResponse({'result':'result'}, status=200)


class DogView(View):
    def post(self, request):
        data    = json.loads(request.body)
        dog     = Dog.objects.create(
            name=data['name'],
            age=data['age'],
            owner=Owner.objects.get(name=data['owner'])
            )
        return JsonResponse({'MESSAGE':'CREATED'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        result = []
        
        for dog in dogs : 
            dog_info = {
                'name'  : dog.name,
                'age'   : dog.age,
                'owner' : dog.owner.name,
            }
            result.append(dog_info)
        return JsonResponse({'result':'result'}, status=200) 