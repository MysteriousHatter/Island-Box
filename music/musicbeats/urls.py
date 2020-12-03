from django.urls import path
from . import views

urlpatterns = [
    path('songs/', views.songs, name='songs'),
    path('songs/<int:id>', views.songpost, name='songpost'),
    path('albums/', views.albums, name='albums'),
    path('albums/<int:id>', views.albumDes, name='albumDescription'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('watchlater', views.watchlater, name='watchlater'),
    path('history', views.history, name='history'),
    path('c/<str:channel>', views.channel, name='channel'),
    path('upload', views.upload, name='upload'),
    path('search', views.upload, name='search'),
    path('artistlogin', views.artistLogin, name='artistlogin'),
    path('artistSignup', views.artistSignUp, name='artistSignup'),
]
