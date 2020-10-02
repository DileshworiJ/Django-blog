from .import views
from django.urls import path

app_name = 'blog'      #allows us to organize url with applications

urlpatterns = [
    path('',views.post_list,name='post_list'),    
path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
]                   