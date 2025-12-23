from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import datetime
from book.models import Book

# Create your views here.
def show_time(request):
    now = datetime.datetime.now()
    html = '<html lang="en"><body>hello friend the time is %s.</body></html>' % now
    return HttpResponse(html)

def pen(request):
    html = '<html lang ="en"><body>this is a pen.</body></html>'
    return HttpResponse(html)

def book1(request):
    html = 'this is book1'
    return HttpResponse(html)

def show_objects(request):
    books = Book.objects.all().values()
    book_list = list(books)
    return JsonResponse(book_list,safe =False)

def show_objects_1(request):
    books = Book.objects.all()
    books_json = serializers.serialize('json', books)
    return HttpResponse(books_json, content_type='application/json')

def show_object_myway(request):
    books = Book.objects.all()
    result = ""
    for i in books:
        result += str(i) +'\n'
    return HttpResponse(result)
