from django.urls import path
from . import views

app_name = 'musicbeats'

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
    path('channel2', views.ChannelListView.as_view(), name='channel-list-view'),
    path('<pk>/', views.ChannelDetailView.as_view(), name='channel-Detail'),
    path('c/<str:channel>', views.channelView, name='channel'),
    path('upload', views.upload, name='upload'),
    path('search', views.upload, name='search'),
    path('switch_follow', views.follow_unfollow_profile, name='follow-unfollow-view'),
]
