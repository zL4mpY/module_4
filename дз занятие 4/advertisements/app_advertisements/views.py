from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<a href=\'lesson_4\'>Перейти на Lesson 4</a>')