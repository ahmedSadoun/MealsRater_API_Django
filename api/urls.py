from django.urls import URLPattern, path
from rest_framework import routers
from django.conf.urls import include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token 
router=routers.DefaultRouter()
router.register('users',UserViewSet)
router.register('meals',MealViewSet)
router.register('rating',RatingViewSet)

urlpatterns=[
    path('',include(router.urls)),
    #wheneverb the user hits this url a token will be generated for this user 
    path('tokenrequest/',obtain_auth_token),
]