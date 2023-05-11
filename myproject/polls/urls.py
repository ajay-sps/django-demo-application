from django.urls import path
from . import views

urlpatterns = [
        path('',views.index,name='homepage'),
        path('softprodigy/',views.softprodigy,name='softprodigy'),
        path('book/',views.book,name='book'),
        path('book/<int:pk>/',views.delete_book,name='delete book'),
]