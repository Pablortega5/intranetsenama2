from django.contrib import admin
from .models import Noticia, Evento, Document, Categoria_inf, Section

# Register your models here.
admin.site.register(Noticia)
admin.site.register(Evento)
admin.site.register(Document)
admin.site.register(Categoria_inf)
admin.site.register(Section)