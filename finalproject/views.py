from django.shortcuts import render
from books.models import book
def info(request):
    books=book.objects.all()
    context={
        'books':books,
    }
    return render(request,'home.html',context)