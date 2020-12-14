from django.shortcuts import render
from django.views import View
from .models import Book
from rest_framework import viewsets
from .serializer import BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    


def fun(request):
    books=Book.objects.all()
    context={'book':books}
    return render(request, "first_temp.html", context)