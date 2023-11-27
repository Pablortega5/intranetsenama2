from django import forms
from .models import CarouselItem, Noticia, Document, Evento, Categoria_doc, Section
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User


class NoticiaForm(forms.ModelForm):
    
    class Meta:
        model= Noticia
        fields = '__all__'

    titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cuerpo = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    imagen = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)
    

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['titulo', 'descripcion', 'categoria', 'archivo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}), 
            'archivo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'fecha', 'horario_inicio', 'horario_fin']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'horario_inicio': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'horario_fin': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),

    }


class CategoriaForm(forms.ModelForm):
    
    class Meta:
        model = Categoria_doc
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),

        }

class CarouselItemForm(forms.ModelForm):
    class Meta:
        model = CarouselItem
        fields = ['image']

    image = forms.ImageField(
        label='Imagen', 
        widget=forms.FileInput(attrs={'class': 'form-control'})
           )


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'
    title = forms.CharField(
        label='Título',  
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    content = forms.CharField(
        label='Contenido',  
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    image = forms.ImageField(
        label='Imagen', 
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

