from django.contrib import admin

# Register your models here.
from sistema.models import Linhas, Categorias, Produtos

class LinhasAdmin(admin.ModelAdmin):

    list_display = ['id', 'nome']
    search_fields = ['id', 'nome']

class CategoriasAdmin(admin.ModelAdmin):

    list_display = ['id', 'nome']
    search_fields = ['id', 'nome']


class ProdutosAdmin(admin.ModelAdmin):

    list_display = ['id', 'nome', 'codigo', 'categoria', 'linha']
    search_fields = ['id', 'nome']

admin.site.register(Linhas, LinhasAdmin)
admin.site.register(Categorias, CategoriasAdmin)
admin.site.register(Produtos, ProdutosAdmin)