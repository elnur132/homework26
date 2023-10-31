from django.forms import ModelForm
from .models import Book
from django.core.exceptions import ValidationError


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'genre')
        
    def clean_name(self):
        name = self.cleaned_data['name']
        for i in name:
            if not i.isupper():
                raise ValidationError("Заголовок должен быть в верхнем регистре")
            return name