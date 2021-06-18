from django.contrib import admin
from .models import Anime, Manga, Autor, Estudio

# Register your models here.

class AnimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'ano_lancamento', 'estudio',)
    list_display_links = ('nome', 'id')
    list_per_page = 4
    search_fields = ('nome', 'nome_alternativo', 'ano_lancamento',)


class MangaAdmin(admin.ModelAdmin):
    list_per_page = 4
    list_display_links = ('nome', 'id')
    list_display = ('id', 'nome', 'ano_lancamento', 'estudio',)
    search_fields = ('nome', 'nome_alternativo', 'estudio',)


admin.site.register(Anime, AnimeAdmin)  #anime
admin.site.register(Manga, MangaAdmin)  #manga
admin.site.register(Autor)
admin.site.register(Estudio)

