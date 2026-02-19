from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def students(request):
    students = {
        "name": "John",
        "age": 20,
        "grade": "A"
    }
    return HttpResponse('Hello, students!')