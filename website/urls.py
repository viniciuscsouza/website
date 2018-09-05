# Importa método path do Django
from django.urls import path

# Importa funções definidas no arquivo views.py
from . import views

# Atributo que define namespace do app website
app_name = 'website'

# Lista de roteamento das URLs
urlpatterns = [
    # GET /
    path('', views.index, name='index'),
    # Cadastra linhas
    path('cadastrar_linhas/', views.cadastrar_linhas, name='cadastrar_linhas'),
    path('consultar_linhas/', views.consultar_linhas, name='consultar_linhas'),
    path('editar_linhas/<int:id>', views.editar_linhas, name='editar_linhas'),
    path('deletar_linhas/<int:id>', views.deletar_linhas, name='deletar_linhas'),
    path('cadastrar_produtos/', views.cadastrar_produtos, name='cadastrar_produtos'),
    path('consultar_produtos/', views.consultar_produtos, name='consultar_produtos'),
    path('editar_produtos/<int:id>', views.editar_produtos, name='editar_produtos'),
    path('deletar_produtos/<int:id>', views.deletar_produtos, name='deletar_produtos'),
    path('cadastrar_categorias/', views.cadastrar_categorias, name='cadastrar_categorias'),
    path('consultar_categorias/', views.consultar_categorias, name='consultar_categorias'),
    path('editar_categorias/<int:id>', views.editar_categorias, name='editar_categorias'),
    path('deletar_categorias/<int:id>', views.deletar_categorias, name='deletar_categorias'),
]