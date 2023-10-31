from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm

# Create your views here.
class BookList(ListView):
    model = Book
    template_name = 'books_list.html'
    context_object_name = 'books'
    
class CreateBook(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'create_books.html'
    succesful_url = reverse_lazy('books')
    
    def clean(self):
        cleaned_data = super().clean() 
        name = cleaned_data.get('name')
        if name: 
            self.clean_name()  