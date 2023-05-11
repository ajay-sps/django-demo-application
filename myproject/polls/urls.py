from django.urls import path
from . import views

urlpatterns = [
        path('',views.index,name='homepage'),
        path('book/',views.book,name='book'),
        path('book/<int:pk>/',views.delete_book,name='delete book'),
]