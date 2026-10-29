from django.db import models
from django.urls import reverse

class Conteudo(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    conteudo_html = models.TextField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Menu(models.Model):
    INTERNO = 'interno'
    EXTERNO = 'externo'
    TIPOS = [
        (INTERNO, 'Conteúdo interno'),
        (EXTERNO, 'Link externo'),
    ]

    titulo = models.CharField(max_length=100)
    tipo_destino = models.CharField(max_length=10, choices=TIPOS)
    ordem = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)
    conteudo = models.ForeignKey(
        Conteudo, null=True, blank=True, on_delete=models.SET_NULL
    )
    url_externa = models.URLField(blank=True)

    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return self.titulo

    def get_url(self):
        if self.tipo_destino == self.INTERNO and self.conteudo:
            return reverse('conteudo', args=[self.conteudo.slug])
        return self.url_externa