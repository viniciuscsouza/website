from django import forms
from .models import Linhas, Categorias, Produtos

class LinhasForm(forms.ModelForm):
    
    class Meta:
        model = Linhas
        fields = "__all__"

class CategoriasForm(forms.ModelForm):

    class Meta:
        model = Categorias
        fields = "__all__"

class ProdutosForm(forms.ModelForm):

    class Meta:
        model = Produtos
        fields = "__all__"