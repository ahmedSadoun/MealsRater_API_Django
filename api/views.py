
from logging import raiseExceptions
from turtle import update
from urllib import request, response
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny , IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    #authentication_classes=[TokenAuthentication]
    permission_classes=[AllowAny]
    def create(self,request,*args,**kawrgs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer=serializer)
        token,created=Token.objects.get_or_create(user=serializer.instance)
        return Response({'token':token.key},status=status.HTTP_201_CREATED)
    def list(self, request, *args, **kwargs):
        response={'message':'You cannot create rating like that '}
        return Response(response,status=status.HTTP_400_BAD_REQUEST)
    def update(self, request, *args, **kwargs):
        response={'message':'You cannot create rating like that '}
        return Response(response,status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, *args, **kwargs):
        response={'message':'You cannot create rating like that '}
        return Response(response,status=status.HTTP_400_BAD_REQUEST)

class MealViewSet(viewsets.ModelViewSet):
    queryset=Meal.objects.all()
    serializer_class=MealSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    @action(methods=['post'],detail=True)
    def rate_meal(self,request,pk=None):
        if 'stars' in request.data:
            #create or update
            meal=Meal.objects.get(id=pk)
            stars=request.data['stars']
            #because of the token is passed through the request i can get the user through it 
            # the the user equal 
            user = request.user
            # username=request.data['username']
            # user=User.objects.get(username=username)

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
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    #override the update function to prevent ANY RATING FROM THIS VIEWSET
    def update(self, request, *args, **kwargs):
        respons={
            'message':'Invalid way to create or update'
        }
        return Response(respons,status=status.HTTP_400_BAD_REQUEST)
    def create(self, request, *args, **kwargs):
        respons={
            'message':'Invalid way to create or update'
        }
        return Response(respons,status=status.HTTP_400_BAD_REQUEST)