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
    path('characters/<int:character_id>/add_photo/', views.add_photo, name='add_photo'),
    path('characters/<int:character_id>/assoc_award/<int:award_id>/', views.assoc_award, name='assoc_award'),
    path('characters/<int:character_id>/unassoc_award/<int:award_id>/', views.unassoc_award, name='unassoc_award'),
    path('awards', views.AwardList.as_view(), name='awards_index'),
    path('awards/<int:pk>', views.AwardDetail.as_view(), name='awards_detail'),
    path('awards/create', views.AwardCreate.as_view(), name='awards_create'),
    path('awards/<int:pk>/update', views.AwardUpdate.as_view(), name='awards_update'),
    path('awards/<int:pk>/delete', views.AwardDelete.as_view(), name='awards_delete'),
]

