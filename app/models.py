from django.db import models



class Categoria_inf(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    imagen = models.ImageField(upload_to='noticias')
    categoria = models.ForeignKey(Categoria_inf, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo
    
class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    fecha = models.DateField()
    horario_inicio = models.CharField(max_length=100)
    horario_fin = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.titulo


    
class Categoria_doc(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
class Document(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    archivo = models.FileField(upload_to='pdfs/')
    categoria = models.ForeignKey(Categoria_doc, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo


class CarouselItem(models.Model):
    image = models.ImageField(upload_to='carousel_images/')
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"CarouselItem - {self.image.name}"

class Section(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='section_images/')
    content = models.TextField()

    def __str__(self):
        return self.title
    

class Banner(models.Model):
    image = models.ImageField(upload_to='banner_images/')
    link = models.URLField()

    def __str__(self):
        return f"Banner - {self.image.name}"