from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name= 'index'),
     path('index.html', views.index, name ='index'),
     path('out-team.html', views.our_team, name = 'out-team'),
     path('profile-page.html', views.profile_page, name = 'profile-page'),
     path('search.html', views.search, name = 'search')

]