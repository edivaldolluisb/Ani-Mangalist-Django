from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:anime_id>', views.ver_detalhe, name='ver_detalhe'),
    path('busca/', views.busca, name='busca'),

    path('manga/', views.manga, name='manga'),
    path('manga/<int:manga_id>', views.manga_detalhe, name='manga_detalhe'),
    path('manga_busca/', views.manga_busca, name='manga_busca'),
]
