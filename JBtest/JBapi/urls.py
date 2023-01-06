from . import views
from django.urls import include, path
from rest_framework import routers

urlpatterns = [
	path('api/posts/', views.post_list),
	path('api/posts/<int:pk>/image', views.get_image) ,
	path('api/posts/<int:pk>', views.post_detail) ,
	path('api/posts/created', views.posts_created),
	path('api/posts/updated', views.posts_updated),
]