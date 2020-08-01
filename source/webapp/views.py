
from django.shortcuts import render, get_object_or_404
from webapp.models import Book


def index_view(request):
    Books = Book.objects.all().filter(status='active').order_by('-created_at')
    context = {
        'Books': Books
    }
    return render(request, 'index.html', context)


def create_view(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        descriptions = request.POST.get('descriptions')
        Books = Book.objects.create(name=name, email=email, descriptions=descriptions)
        context = {
            'Books': Books
        }
        return render(request, 'index.html', context)




