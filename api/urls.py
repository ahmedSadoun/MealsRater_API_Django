from django.urls import URLPattern, path
from rest_framework import routers
from django.conf.urls import include
from .views import *
router=routers.DefaultRouter()
router.register('meals',MealViewSet)
router.register('rating',RatingViewSet)

urlpatterns=[
    path('',include(router.urls)),
]