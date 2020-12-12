from django.urls import path
from . import views
from .views import Another

urlpatterns = [
    path('', views.fun),
    path('another', Another.as_view()),
]
