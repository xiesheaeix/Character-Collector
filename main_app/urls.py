from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('characters/',views.characters_index, name='index'),
    path('characters/<int:character_id>/', views.characters_detail, name='detail'),
    path('characters/create/', views.CharacterCreate.as_view(), name='character_create'),
    path('characters/<int:pk>/update/', views.CharacterUpdate.as_view(), name='character_update'),
    path('characters/<int:pk>/delete/', views.CharacterDelete.as_view(), name='character_delete'),
    path('characters/<int:character_id>/add_token/', views.add_token, name='add_token'),

]

