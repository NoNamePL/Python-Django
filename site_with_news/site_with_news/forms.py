from .models import New
from django.forms import ModelForm, TextInput, Textarea


class NewForm(ModelForm):
    class Meta:
        model = New
        fields = ['title', 'new_text']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите название"
            }),
            "new_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введите описание"
            }),

        }
