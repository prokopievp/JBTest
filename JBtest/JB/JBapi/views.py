from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import FileResponse
from django.contrib import admin
from .models import Post
from .serializers import PostSerializer
from .image import load_img
import os


###GET and POST for URL like "http://localhost:8000/posts/". Responses all elements.
@api_view(['GET', 'POST'])
def post_list(request):
	if request.method == 'GET':
		posts = Post.objects.all()
		serializer = PostSerializer(posts, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = PostSerializer(data=request.data)
		if serializer.is_valid():
			#Downloading image on server in path ".../JBtest/JB/JBapi/image_files". 
			load_img_status = load_img(request.data['imageURL'], Response)
			if load_img_status != None:
				return load_img_status
			
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


###Detailed GET, PUT, DELETE and PATCH for URL like "http://localhost:8000/posts/pk", 
###where pk is id of element in database
@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def post_detail(request, pk):
	try:
		post = Post.objects.get(pk=pk)
	except Post.DoesNotExist:
		#print('NO ELEMENT FOR ID "' + str(pk) + '"')
		return Response('NO ELEMENT FOR ID "' + str(pk) + '"',status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = PostSerializer(post)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = PostSerializer(post, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		post.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	elif request.method == 'PATCH':
		serializer = PostSerializer(post, data=request.data, partial=True)

		if serializer.is_valid():
			if 'imageURL' in request.data:
				#Redownloading image on server in path ".../JBtest/JB/JBapi/image_files"
				load_img_status = load_img(request.data['imageURL'], Response)
				if load_img_status != None:
					return load_img_status
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)



### Responsing binary image from URL like "http://localhost:8000/posts/96/image". pk - id in database.
### Images located on server, path - ".../JBtest/JB/JBapi/image_files"
@api_view(['GET'])
def get_image(request, pk):
	try:
		post = Post.objects.get(pk=pk)
	except Post.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)


	serializer = PostSerializer(post)
	path_to_image = os.getcwd() + '\\JBapi\\image_files\\' + serializer.data['imageURL'].split('/')[-1]
	return FileResponse(open(path_to_image, 'rb'))



###Gettind all elements in database ordered by creation time.
@api_view(['GET'])
def posts_created(request):
	posts = Post.objects.all().order_by('-createdAt')
	serializer = PostSerializer(posts, many=True)
	return Response(serializer.data)



###Gettind all elements in database ordered by last updating time.
@api_view(['GET'])
def posts_updated(request):
	posts = Post.objects.all().order_by('-updatedAt')
	serializer = PostSerializer(posts, many=True)
	return Response(serializer.data)