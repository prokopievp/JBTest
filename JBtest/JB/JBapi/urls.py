from . import views
from django.urls import include, path
from rest_framework import routers

urlpatterns = [
	path('posts/', views.post_list),
	path('posts/<int:pk>/image', views.get_image) ,
	path('posts/<int:pk>', views.post_detail) ,
	path('posts/created', views.posts_created),
	path('posts/updated', views.posts_updated),
]