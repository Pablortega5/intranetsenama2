from django import forms
from .models import Banner, CarouselItem, Noticia, Document, Evento, Categoria_doc, Section
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User


class NoticiaForm(forms.ModelForm):
    
    class Meta:
        model= Noticia
        fields = '__all__'
        
    widgets = {
        'titulo': forms.TextInput(attrs={'class': 'form-control'}),
        'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
        'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        'link': forms.URLInput(attrs={'class': 'form-control'}),
    }

    titulo = forms.CharField(widget=widgets['titulo'])
    cuerpo = forms.CharField(widget=widgets['cuerpo'])
    imagen = forms.ImageField(widget=widgets['imagen'], required=False)
    link = forms.URLField(widget=widgets['link'], required=False)
    

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
    
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")

        # Validación: La contraseña debe tener al menos 8 caracteres.
        if len(password1) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")

        # Validación: La contraseña no puede asemejarse tanto a la otra información personal.
        user_info = [self.cleaned_data.get("username"), self.cleaned_data.get("first_name"), self.cleaned_data.get("last_name"), self.cleaned_data.get("email")]
        for info in user_info:
            if info and info.lower() in password1.lower():
                raise forms.ValidationError("La contraseña no puede asemejarse tanto a su otra información personal.")

        # Validación: La contraseña no puede ser una clave utilizada comúnmente.
        common_passwords = ["123456", "password", "qwerty", "123456789", "12345678"]  # Puedes agregar más contraseñas comunes según tus necesidades
        if password1.lower() in common_passwords:
            raise forms.ValidationError("La contraseña no puede ser una clave utilizada comúnmente.")

        # Validación: La contraseña no puede ser completamente numérica.
        if password1.isdigit():
            raise forms.ValidationError("La contraseña no puede ser completamente numérica.")

        return password1


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
        fields = ['image', 'link']  

    image = forms.ImageField(
        label='Imagen',
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

    link = forms.URLField(
        label='Enlace',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False  
    )

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['image', 'link']

    image = forms.ImageField(
        label='Imagen',
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

    link = forms.URLField(
        label='Enlace',
        widget=forms.TextInput(attrs={'class': 'form-control'})
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

