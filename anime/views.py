from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Anime, Manga, Autor
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat

# api imports
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import AnimeSerializer, MangaSerializer, AutorSerializer

# Create your views here.


#  Views de animes

def index(request):
    animes = Anime.objects.order_by('nome')
    paginator = Paginator(animes, 10)

    page = request.GET.get('p')
    animes = paginator.get_page(page)
    return render(request, 'animes/index.html', {
        'animes': animes
    })


def ver_detalhe(request, anime_id):
    #anime = Anime.objects.get(id=anime_id)
    anime = get_object_or_404(Anime, id=anime_id)
    return render(request, 'animes/ver_detalhe.html', {
        'anime': anime
    })


def busca(request):
    termo = request.GET.get('termo')

    #if termo is None or not termo:
        #raise Http404()

    animes = Anime.objects.order_by('nome').filter(
        Q(nome__icontains=termo) | Q(nome_alternativo__icontains=termo) | Q(autor__nome__icontains=termo),
    )
    if termo is None or not termo:
        animes = Anime.objects.order_by('nome')
    paginator = Paginator(animes, 10)

    page = request.GET.get('p')
    animes = paginator.get_page(page)

    return render(request, 'animes/busca.html', {
        'animes': animes
    })


#  Views de mangas

def manga(request):
    mangas = Manga.objects.order_by('nome')
    paginator = Paginator(mangas, 10)

    page = request.GET.get('p')
    mangas = paginator.get_page(page)
    return render(request, 'animes/manga.html', {
        'mangas': mangas
    })


def manga_detalhe(request, manga_id):
    #anime = Anime.objects.get(id=anime_id)
    manga = get_object_or_404(Manga, id=manga_id)
    return render(request, 'animes/manga_detalhe.html', {
        'manga': manga
    })

def manga_busca(request):
    termo = request.GET.get('termo')

    #if termo is None or not termo:
        #raise Http404()

    mangas = Manga.objects.order_by('nome').filter(
        Q(nome__icontains=termo) | Q(nome_alternativo__icontains=termo) | Q(autor__nome__icontains=termo),
    )
    if termo is None or not termo:
        mangas = Manga.objects.order_by('nome')
    paginator = Paginator(mangas, 10)

    page = request.GET.get('p')
    mangas = paginator.get_page(page)

    return render(request, 'animes/busca_manga.html', {
        'mangas': mangas
    })


# API


@api_view(['GET'])
def animeapiOverview(request):
    api_urls = {
        'List anime':'/anime-list/',
        'Detail anime View':'/anime-detail/<str:pk>/',

        'List manga': '/manga-list/',
        'Detail manga View': '/manga-detail/<str:pk>/',

        'List autor': '/autor-list/',
    }
    return Response(api_urls)


@api_view(['GET'])
def animeList(request):
    animes = Anime.objects.all()
    serializer = AnimeSerializer(animes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def animeDetail(request, pk):
    animes = Anime.objects.get(id=pk)
    serializer = AnimeSerializer(animes, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def mangaList(request):
    mangas = Manga.objects.all()
    serializer = MangaSerializer(mangas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def mangaDetail(request, pk):
    mangas = Manga.objects.get(id=pk)
    serializer = MangaSerializer(mangas, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def autorList(request):
    autores = Autor.objects.all()
    serializer = AutorSerializer(autores, many=True)
    return Response(serializer.data)