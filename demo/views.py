from django.shortcuts import render
from django.views import View
from .models import Book
from rest_framework import viewsets
from .serializer import BookSerializer, BookMiniSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookMiniSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def retrieve(self, *args, **kwargs):
        instance=self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)
    


def fun(request):
    books=Book.objects.all()
    context={'book':books}
    return render(request, "first_temp.html", context)