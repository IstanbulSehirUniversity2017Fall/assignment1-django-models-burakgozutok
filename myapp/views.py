
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from models import Author, Book

# Create your views here.


def index(request):
    return HttpResponse("<h1>Main Page<h1>")

def book_details(request, book_id):
    bookObjects = Book.objects.all()
    book_id = int(book_id)
    if(book_id < len(bookObjects)):
        elementValues = Book.objects.all()[book_id]
        return HttpResponse("<h2>Book number %s detail page.</h2> <br/>" \
                            "<b>Name:</b> %s</h2> <br/>" \
                            "<b>Author:</b> %s</h2> <br/>" \
                            "<b>ISBN:</b> %s</h2> <br/>" \
                            "<b>Publish Date:</b> %s</h2> <br/>" \
                            "<b>Author:</b> %s"
                            ""% (str(book_id),elementValues.name, elementValues.author, elementValues.isbnNumber, elementValues.publishdate, elementValues.author   ))
    else:
        return HttpResponse("<h1>Book with id %s is not found!</h1>" % str(book_id))