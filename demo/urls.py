from django.urls import path, include
from .views import BookViewSet
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('book', BookViewSet)

urlpatterns = [
    path('', views.fun),
    path('b', views.BookViewSet.as_view({'get': 'list'})),
    path('s', include(router.urls))
]
