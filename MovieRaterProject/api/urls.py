
from django.urls import path, include
from rest_framework import routers
from .views import MovieViewSet, RatingViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('movie', MovieViewSet)
router.register('rating', RatingViewSet)
router.register('user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
