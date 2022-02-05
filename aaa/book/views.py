from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone

from book.models import Books
# Create your views here.

def index(request):
    # latest_books_list = Books.objects.all().order_by('id')
    # context = {'latest_books_list': latest_books_list}
    #return render(request, 'book/index.html', context)
    if request.method == "GET" and request.GET.get('search'):
        print(request.GET)
        latest_books_list=Books.objects.filter(Book_name__contains=request.GET.get('search'))
        
    else:
        latest_books_list = Books.objects.all().order_by('id')

    context = {'latest_books_list': latest_books_list}
    return render(request, 'book/index.html', context)

    
def detail(request, books_id):
   
    book_info = get_object_or_404(Books, pk=books_id)
    context = {'book_info': book_info}
    return render(request, 'book/detail.html', context)
    
def add(request):
    if request.method == "POST":
    
        qry = Books(Book_name=request.POST['Book_name'], Writer=request.POST['Writer'])
        qry.save()
        return HttpResponseRedirect(reverse('book:index'))
    else:
        return render(request, 'book/add.html')
        
def update(request, books_id):
    if request.method == "POST":
        selected_qry = Books.objects.get(pk=books_id)
        selected_qry.Book_name=request.POST['Book_name']
        selected_qry.Publishing_date=request.POST['Publishing_date']
        selected_qry.Price=request.POST['Price']
        selected_qry.Intro_book=request.POST['Intro_book']
        selected_qry.save()
        return HttpResponseRedirect(reverse('book:index'))
    else:
        books = get_object_or_404(Books, pk=books_id)
        return render(request, 'book/update.html', {'Books':books})        
        
def remove(request, books_id):
    Books.objects.get(pk=books_id).delete()

    return	HttpResponseRedirect(reverse('book:index'))	