from django.db import models

# Create your models here.

class Linhas(models.Model):
    nome = models.CharField('Nome', max_length =100, null=False, blank=False)

    class Meta:
        verbose_name = 'Linha'
        verbose_name_plural = 'Linhas'
        ordering = ['nome']


    def __str__(self):
        return self.nome

class Categorias(models.Model):
    nome = models.CharField('Nome', max_length =100, null=False, blank=False)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome

class Produtos(models.Model):
    codigo = models.CharField('Produto', max_length = 10, null=False, blank=False)
    nome = models.CharField('Nome', max_length =100, null=False, blank=False)
    categoria = models.ForeignKey(
        Categorias, 
        on_delete=models.CASCADE, 
        verbose_name='Categoria',
        default='categoria'
        )
    linha = models.ForeignKey(
        Linhas, 
        on_delete=models.CASCADE, 
        verbose_name='Linha',
        default='linha'
        )

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome


