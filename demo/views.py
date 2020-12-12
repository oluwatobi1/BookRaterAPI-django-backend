from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book

# Create your views here.
class Another(View):
    books = Book.objects.get(id=1)
    out = f'we have {books.title } in database with id {books.id}<br>'

    # for each in books:
    #     out += f'we have {each.title } in database<br>'

    def get(self, request):
        return HttpResponse(self.out)

def fun(request):
    return HttpResponse("Hello WOrld")