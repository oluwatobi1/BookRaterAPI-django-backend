from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Book


def fun(request):
    return render(request, "first_temp.html")