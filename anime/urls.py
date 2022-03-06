from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:anime_id>', views.ver_detalhe, name='ver_detalhe'),
    path('busca/', views.busca, name='busca'),

    path('manga/', views.manga, name='manga'),
    path('manga/<int:manga_id>', views.manga_detalhe, name='manga_detalhe'),
    path('manga_busca/', views.manga_busca, name='manga_busca'),

    # API's
    path('anime_api/', views.animeapiOverview, name='anime-api'),
    path('anime-list/', views.animeList, name='animelist'),
    path('anime-detail/<str:pk>/', views.animeDetail, name='animedetail'),

    path('manga-list/', views.mangaList, name='mangalist'),
    path('manga-detail/<str:pk>/', views.mangaDetail, name='mangadetail'),
]
