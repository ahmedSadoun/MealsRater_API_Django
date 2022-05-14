
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','password')
        #to prevent the password from returning in the response , just we can create a pssword not to read 
        extra_kwargs = {
            
            'password': {'write_only': True , 'required':True}
        }
    

        
class MealSerializer(serializers.ModelSerializer):
    class Meta :
        model=Meal
        fields=('id','title','description','no_of_ratings','avg_rating')
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields=('id','stars','user','meal')