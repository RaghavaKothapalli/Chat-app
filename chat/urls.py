from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat_room, name='chat'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register')  # register view
]
