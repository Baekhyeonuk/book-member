from django.urls import path
from book import views


app_name = 'book'
urlpatterns = [
    path('', views.index, name='index'), 
    ## 
    path('<int:books_id>/detail/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
    path('<int:books_id>/remove/', views.remove, name='remove'),
    path('<int:books_id>/update/', views.update, name='update'), 
    
]