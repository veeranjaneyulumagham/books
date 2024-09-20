from django.shortcuts import render,get_object_or_404
from books.models import book
# Create your views here.
def books_details(request,pk):
    books=get_object_or_404(book,pk=pk)
    context={
        'books':books,
    }
    return render(request,'books_details.html',context)