
from urllib import response
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
# Create your views here.
class MealViewSet(viewsets.ModelViewSet):
    queryset=Meal.objects.all()
    serializer_class=MealSerializer
    @action(methods=['post'],detail=True)
    def rate_meal(self,request,pk=None):
        if 'stars' in request.data:
            #create or update
            meal=Meal.objects.get(id=pk)
            stars=request.data['stars']
            username=request.data['username']
            user=User.objects.get(username=username)

            try:
                #update
                rate = Rating.objects.get(user=user.id,meal=meal.id)
                rate.stars=stars
                rate.save()
                serializer=RatingSerializer(rate , many=False)
                json={
                    'message':'Meal Rate Updated',
                    'result':serializer.data
                }
                return Response(json)
            except:
                #create
                rate= Rating()
                # or create with Rating.objects.create(user=user,meal=meal,stars=stars)
                rate.user=user
                rate.meal=meal
                rate.stars=stars
                rate.save()
                serializer=RatingSerializer(rate , many=False)
                json={
                    'message':'Meal Rate Created',
                    'result':serializer.data
                }
                return Response(json,status=status.HTTP_201_CREATED)
        else :
            
            json={
                'message':'No stars Provided'
            }
            return Response(json,status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset=Rating.objects.all()
    serializer_class=RatingSerializer