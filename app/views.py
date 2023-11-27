from django.shortcuts import render, redirect, get_object_or_404
from .models import CarouselItem, Noticia,Evento, Document, Categoria_doc, Section
from datetime import date
from .forms import CustomUserCreationForm, EventoForm, NoticiaForm, DocumentForm, CategoriaForm, CarouselItemForm, SectionForm
from django.db.models import F
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.models import Group
# Create your views here.



def home(request):
    noticias = Noticia.objects.order_by('-fecha_creacion')[:5]
    eventos = Evento.objects.all().order_by('fecha')
    eventos_proximos = eventos.filter(fecha__gte=date.today())[:5]
    documentos = Document.objects.all()
    carousel_items = CarouselItem.objects.all()
    sections = Section.objects.all()

    data = {
        'noticias': noticias,
        'eventos': eventos_proximos,
        'documentos': documentos,
        'carousel_items': carousel_items,
        'sections': sections
    }

    return render(request, 'app/home.html', data)
@permission_required('app.add_noticia')
def crear_noticia(request):
        data = {
                'form': NoticiaForm()
        }
        if request.method == 'POST':
                formulario = NoticiaForm(data=request.POST, files=request.FILES)
                if formulario.is_valid():
                        formulario.save()
                        data["mensaje"] = "Noticia Creada"
                        return redirect(to="listar_noticias")
                else:
                        data["form"] = formulario
                        print(formulario.errors)

        return render (request,'app/noticia/crear.html', data)
@permission_required('app.add_noticia')
def listar_noticias(request):
    noticias = Noticia.objects.order_by('-fecha_creacion')  
    return render(request, 'app/noticia/listar.html', {'noticias': noticias})
@permission_required('app.add_noticia')
def editar_noticia(request, id):
       
        noticia = get_object_or_404(Noticia, id=id)

        data = {
              'form': NoticiaForm(instance=noticia)
        }
        if request.method == 'POST':
                formulario = NoticiaForm(data=request.POST, instance=noticia, files=request.FILES)
                if formulario.is_valid():
                        formulario.save()
                        messages.success(request, "Modificado Correctamente")
                        return redirect(to="listar_noticias")
                data['form']= formulario

        return render(request, 'app/noticia/editar.html', data)
@permission_required('app.delete_noticia')
def eliminar_noticia(request, id):
        noticia = get_object_or_404(Noticia, id=id)
        noticia.delete()
        return redirect(to="listar_noticias")
@permission_required('app.add_document')
def crear_documento(request):
        data = {
                'form': DocumentForm()
        }
        if request.method == 'POST':
                formulario = DocumentForm(data=request.POST, files=request.FILES)
                if formulario.is_valid():
                        formulario.save()
                        data["mensaje"] = "Documento subido"
                        return redirect(to="listar_documentos")
                else:
                        data["form"] = formulario
                        print(formulario.errors)

        return render (request,'app/documento/crear.html', data)
@permission_required('app.add_document')
def listar_documentos(request):
    categoria_id = request.GET.get('categoria', None)
    termino_busqueda = request.GET.get('q', None)

    documentos = Document.objects.all()

    if categoria_id:
        documentos = documentos.filter(categoria_id=categoria_id)

    if termino_busqueda:
        documentos = documentos.filter(Q(titulo__icontains=termino_busqueda))

    categorias = Categoria_doc.objects.all()
    
    data = {
        'documentos': documentos,
        'categorias': categorias,
    }

    return render(request, 'app/documento/listar.html', data)
@permission_required('app.add_document')
def editar_documento(request, id):
       
        documento = get_object_or_404(Document, id=id)

        data = {
              'form': DocumentForm(instance=documento)
        }
        if request.method == 'POST':
                formulario = DocumentForm(data=request.POST, instance=documento, files=request.FILES)
                if formulario.is_valid():
                        formulario.save()
                        return redirect(to="listar_documentos")
                data['form']= formulario

        return render(request, 'app/documento/editar.html', data)
@permission_required('app.delete_document')
def eliminar_documento (request, id):
        documento = get_object_or_404(Document, id=id)
        documento.delete()
        return redirect(to="listar_documentos")
@permission_required('app.add_evento')
def crear_evento(request):
        data = {
                'form': EventoForm()
        }
        if request.method == 'POST':
                formulario = EventoForm(data=request.POST)
                if formulario.is_valid():
                        formulario.save()
                        return redirect(to="listar_eventos")
                else:
                        data["form"] = formulario
                        print(formulario.errors)

        return render (request,'app/evento/crear.html', data)
@permission_required('app.add_evento')
def listar_eventos(request):
        eventos = Evento.objects.order_by('fecha')
        data = {
                'eventos': eventos,
                
        }
        return render(request, 'app/evento/listar.html', data)
@permission_required('app.add_evento')
def editar_evento(request, id):
       
        evento = get_object_or_404(Evento, id=id)

        data = {
              'form': EventoForm(instance=evento)
        }
        if request.method == 'POST':
                formulario = EventoForm(data=request.POST, instance=evento)
                if formulario.is_valid():
                        formulario.save()
                        return redirect(to="listar_eventos")
                data['form']= formulario

        return render(request, 'app/evento/editar.html', data)
@permission_required('app.delete_evento')
def eliminar_evento (request, id):
        evento = get_object_or_404(Evento, id=id)
        evento.delete()
        return redirect(to="listar_eventos")
@permission_required('app.add_user')
def registro(request):
     data = {
          'form': CustomUserCreationForm()
     }

     if request.method == 'POST':
          formulario = CustomUserCreationForm(data=request.POST)
          if formulario.is_valid():
               formulario.save()
               user = authenticate(username=formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"] )
               messages.success(request, "Registro completado")
               return redirect (to="listar_usuarios")
          data["form"] = formulario

     return render (request, 'registration/registro.html', data)

@login_required
def admin(request): 

        return render(request, 'app/admin.html')
@permission_required('app.add_categoria')
def crear_categoria(request):
        data = {
                'form': CategoriaForm()
        }
        if request.method == 'POST':
                formulario = CategoriaForm(data=request.POST)
                if formulario.is_valid():
                        formulario.save()
                        data["mensaje"] = "Documento subido"
                        return redirect(to="listar_categorias")
                else:
                        data["form"] = formulario
                        print(formulario.errors)

        return render (request,'app/categoria/crear.html', data)
@permission_required('app.add_categoria')
def listar_categorias(request):
        categorias = Categoria_doc.objects.all 
        
        data = {
                'categorias': categorias,
                

        }
        return render(request, 'app/categoria/listar.html', data)
@permission_required('app.add_categoria')
def editar_categoria(request, id):
       
        categoria = get_object_or_404(Categoria_doc, id=id)

        data = {
              'form': CategoriaForm(instance=categoria)
        }
        if request.method == 'POST':
                formulario = CategoriaForm(data=request.POST, instance=categoria)
                if formulario.is_valid():
                        formulario.save()
                        return redirect(to="listar_categorias")
                data['form']= formulario

        return render(request, 'app/categoria/editar.html', data)

@permission_required('app.delete_categoria')
def eliminar_categoria (request, id):
        categoria = get_object_or_404(Categoria_doc, id=id)
        categoria.delete()
        return redirect(to="listar_categorias")

@permission_required('app.add_user')
def listar_usuarios(request):
    # Obtener la lista de usuarios ordenados por id
    usuarios = User.objects.all().order_by('id')

    # Obtener todos los grupos de permisos disponibles
    grupos_permisos = Group.objects.all()

    if request.method == 'POST':
        # Procesar el formulario cuando se envía
        usuario_id = request.POST.get('usuario_id')
        grupo_seleccionado_id = request.POST.get('grupo_permisos')

        try:
            usuario = User.objects.get(id=usuario_id)
            grupo_seleccionado = Group.objects.get(id=grupo_seleccionado_id)
            usuario.groups.set([grupo_seleccionado])
            messages.success(request, f'Grupo de permisos asignado con éxito a {usuario.username}')
        except User.DoesNotExist or Group.DoesNotExist:
            messages.error(request, 'Error al asignar el grupo de permisos.')

        return redirect('listar_usuarios')  # Redirigir a la misma página después de procesar el formulario

    # Crear un diccionario con los datos que se pasarán al template
    data = {
        'usuarios': usuarios,
        'grupos_permisos': grupos_permisos,
    }

    # Renderizar el template y pasar los datos
    return render(request, "registration/listar.html", data)


@permission_required('app.add_user')
def eliminar_usuario(request, id):
    usuario = get_object_or_404(User, id=id)
    usuario.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_usuarios")

@permission_required('app.add_user')
def editar_usuario(request, id):
    usuario = get_object_or_404(User, id=id)

    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Actualizado correctamente")
            return redirect('listar_usuarios')
    else:
        formulario = CustomUserCreationForm(instance=usuario)

    data = {
        'form': formulario
    }

    return render(request, "registration/actualizar_usuario.html", data)

def listar_noticias_home(request):
    noticias = Noticia.objects.order_by('-fecha_creacion')  
    return render(request, 'app/home/listar_noticias.html', {'noticias': noticias})

def ver_noticia(request, id):
    # Recupera la noticia desde la base de datos por su ID
    noticia = get_object_or_404(Noticia, id=id)

    # Renderiza una plantilla para mostrar la noticia completa
    return render(request, 'app/noticia/ver_noticia.html', {'noticia': noticia})

def listar_eventos_home(request):
        eventos = Evento.objects.order_by('fecha')
        data = {
                'eventos': eventos,
                
        }
        return render(request, 'app/home/listar_eventos.html', data)

def listar_documentos_home(request):
    categoria_id = request.GET.get('categoria', None)
    termino_busqueda = request.GET.get('q', None)

    documentos = Document.objects.all()

    if categoria_id:
        documentos = documentos.filter(categoria_id=categoria_id)

    if termino_busqueda:
        documentos = documentos.filter(Q(titulo__icontains=termino_busqueda))

    categorias = Categoria_doc.objects.all()
    
    data = {
        'documentos': documentos,
        'categorias': categorias,
    }

    return render(request, 'app/home/listar_documentos.html', data)


def add_image(request):
    if request.method == 'POST':
        form = CarouselItemForm(request.POST, request.FILES)
        if form.is_valid():
            # Guarda la imagen en el modelo del carrusel
            image = form.cleaned_data['image']
            CarouselItem.objects.create(image=image)
            return redirect('listar_imagenes')  
    else:
        form = CarouselItemForm()

    return render(request, 'app/carrusel/crear.html', {'form': form})


def listar_imagenes(request):
    images = CarouselItem.objects.all()
    return render(request, 'app/carrusel/listar.html', {'images': images})

@permission_required('app.delete_categoria')
def eliminar_imagen(request, image_id):
    image = CarouselItem.objects.get(pk=image_id)
    image.delete()
    return redirect('listar_imagenes')

def section_create(request):
    if request.method == 'POST':
        form = SectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('section_list')
    else:
        form = SectionForm()
    return render(request, 'app/acordeon/crear.html', {'form': form})

def section_list(request):
    sections = Section.objects.all()
    return render(request, 'app/acordeon/listar.html', {'sections': sections})

def section_edit(request, section_id):
    section = get_object_or_404(Section, pk=section_id)
    if request.method == 'POST':
        form = SectionForm(request.POST, request.FILES, instance=section)
        if form.is_valid():
            form.save()
            return redirect('section_list')
    else:
        form = SectionForm(instance=section)
    return render(request, 'app/acordeon/editar.html', {'form': form, 'action': 'Editar'})

@permission_required('app.delete_categoria')
def section_delete(request, section_id):
    section = get_object_or_404(Section, pk=section_id)
    section.delete()
    return redirect('section_list')