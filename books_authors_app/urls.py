from django.urls import path
from . import views
urlpatterns = [
    path('', views.principal_libros),
    path('authors/', views.principal_autores),
    path('crearl', views.crearlibro),
    path('authors/creara', views.crearautor),
    path('books/<int:num>/', views.rutasl),
    path('asociarl', views.asociar_libro),
    path('authors/authors/<int:num>/', views.rutasa),
    path('asociara', views.asociar_autor),
    ]

