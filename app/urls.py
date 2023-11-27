from django.urls import path


from .views import (
    add_image,
    crear_categoria,
    crear_evento,
    editar_categoria,
    editar_documento,
    editar_evento,
    editar_usuario,
    eliminar_categoria,
    eliminar_documento,
    eliminar_evento,
    eliminar_imagen,
    eliminar_usuario,
    home,
    crear_noticia,
    listar_categorias,
    listar_documentos_home,
    listar_eventos,
    listar_eventos_home,
    listar_imagenes,
    listar_noticias,
    editar_noticia,
    eliminar_noticia,
    crear_documento,
    listar_noticias_home,
    listar_usuarios,
    registro,
    admin,
    listar_documentos,
    section_create,
    section_delete,
    section_edit,
    section_list,
    ver_noticia
)

urlpatterns = [
    path("", home, name="home"),
    path("crear_noticia/", crear_noticia, name="crear_noticia"),
    path("listar_noticias/", listar_noticias, name="listar_noticias"),
    path("editar_noticia/<id>/", editar_noticia, name="editar_noticia"),
    path("eliminar_noticia/<id>/", eliminar_noticia, name="eliminar_noticia"),
    path("crear_documento/", crear_documento, name="crear_documento"),
    path("listar_documentos/", listar_documentos, name="listar_documentos"),
    path("editar_documento/<id>/", editar_documento, name="editar_documento"),
    path("eliminar_documento/<id>/", eliminar_documento, name="eliminar_documento"),
    path("crear_evento/", crear_evento, name="crear_evento"),
    path("listar_eventos/", listar_eventos, name="listar_eventos"),
    path("editar_evento/<id>/", editar_evento, name="editar_evento"),
    path("eliminar_evento/<id>/", eliminar_evento, name="eliminar_evento"),
    path("registrar_usuario/", registro, name="registrar_usuario"),
    path("adm/", admin, name="adm"),
    path("crear_categoria/", crear_categoria, name="crear_categoria"),
    path("listar_categorias/", listar_categorias, name="listar_categorias"),
    path("editar_categoria/<id>/", editar_categoria, name="editar_categoria"),
    path("eliminar_categoria/<id>/", eliminar_categoria, name="eliminar_categoria"),
    path('listar_usuarios/', listar_usuarios, name='listar_usuarios'),
    path('eliminar_usuario/<id>/', eliminar_usuario, name= "eliminar_usuario"),
    path('editar_usuario/<id>/', editar_usuario, name= "editar_usuario"),
    path("listar_noticias_home/", listar_noticias_home, name="listar_noticias_home"),
    path('ver_noticia/<id>/', ver_noticia, name='ver_noticia'),
    path("listar_eventos_home/", listar_eventos_home, name="listar_eventos_home"),
    path("listar_documentos_home/", listar_documentos_home, name="listar_documentos_home"),
    path('add_image/', add_image, name='add_image'),
    path('listar_imagenes/', listar_imagenes, name='listar_imagenes'),
    path('eliminar_imagen/<int:image_id>/', eliminar_imagen, name='eliminar_imagen'),
    path('section_create/', section_create, name='section_create'),
    path('section_list/', section_list, name='section_list'),
    path('section_edit/<int:section_id>/', section_edit, name='section_edit'),
    path('section_delete/<int:section_id>/', section_delete, name='section_delete'),
    
]
