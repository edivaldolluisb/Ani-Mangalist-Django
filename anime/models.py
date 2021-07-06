from django.db import models
from django.utils import timezone

# Create your models here.


class Autor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Estudio(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Anime(models.Model):
    nome = models.CharField(max_length=150)
    nome_alternativo = models.CharField(max_length=150, blank=True)
    ano_lancamento = models.DateField(default=timezone.now)
    autor = models.ForeignKey(Autor, on_delete=models.DO_NOTHING, default=4)
    foto = models.ImageField(blank=True, upload_to='fotos/fotos_anime/%Y%m%d')

    '''def autores(self):
        return ','.join([autor.nome for autor in self.autor.all])'''

    def __str__(self):
        return self.nome


class Manga(models.Model):
    nome = models.CharField(max_length=150)
    nome_alternativo = models.CharField(max_length=150, blank=True)
    ano_lancamento = models.DateField(default=timezone.now)
    autor = models.ForeignKey(Autor, on_delete=models.DO_NOTHING, default=4)
    estudio = models.ManyToManyField(Estudio)
    foto = models.ImageField(blank=True, upload_to='fotos/fotos_manga/%Y%m%d')

    def estudios(self):
        return ','.join([estudio.nome for estudio in self.estudio.all])

    '''def autores(self):
        return ','.join([autor.nome for autor in self.autor.all])'''

    def __str__(self):
        return self.nome

