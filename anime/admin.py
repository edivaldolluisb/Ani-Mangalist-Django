from django.contrib import admin
from .models import Anime, Manga, Autor, Estudio

# Register your models here.

class AnimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'ano_lancamento', 'autor',)
    list_display_links = ('nome', 'id')
    list_per_page = 20
    search_fields = ('nome', 'nome_alternativo', 'autor', 'ano_lancamento',)


class MangaAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display_links = ('nome', 'id')
    list_display = ('id', 'nome', 'ano_lancamento', 'autor',)
    search_fields = ('nome', 'nome_alternativo', 'autor', 'ano_lancamento')


admin.site.register(Anime, AnimeAdmin)  #anime
admin.site.register(Manga, MangaAdmin)  #manga
admin.site.register(Autor)
admin.site.register(Estudio)

