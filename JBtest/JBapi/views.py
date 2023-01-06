from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import FileResponse
from django.contrib import admin
from .models import Post
from .serializers import PostSerializer
from .image import load_img
import os


###GET and POST for URL like "http://localhost:8000/api/posts/". Responses all elements.
@api_view(['GET', 'POST', 'DELETE'])
def post_list(request):
	if request.method == 'GET':
		posts = Post.objects.all()
		serializer = PostSerializer(posts, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	elif request.method == 'POST':
		serializer = PostSerializer(data=request.data)
		if serializer.is_valid():
			#Downloading image on server in path ".../JBtest/image_files". 
			load_img_status = load_img(request.data['imageURL'], Response)
			if load_img_status != None:
				return load_img_status
			
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		posts = Post.objects.all()
		posts.delete()
		images_dir = os.getcwd() + '\\JBapi\\image_files'
		for f in os.listdir(images_dir):
			os.remove(os.path.join(images_dir, f))
		return Response(status=status.HTTP_204_NO_CONTENT)


###Detailed GET, PUT, DELETE and PATCH for URL like "http://localhost:8000/api/posts/pk", 
###where pk is id of element in database
@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def post_detail(request, pk):
	try:
		post = Post.objects.get(pk=pk)
	except Post.DoesNotExist:
		return Response([], status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = PostSerializer(post)
		return Response(serializer.data, status=status.HTTP_200_OK)

	elif request.method == 'PUT':
		old_image_url = post['imageURL']
		serializer = PostSerializer(post, data=request.data)
		if serializer.is_valid():
			#Downloading image on server in path ".../JBtest/JBapi/image_files".
			new_image_url =  request.data['imageURL']
			load_img_status = load_img(new_image_url, Response)
			if load_img_status != None:
				return load_img_status
			if new_image_url != old_image_url:
				image_file_name = old_image_url.split('/')[-1]
				image_path = os.getcwd() + '\\JBapi\\image_files\\' + image_file_name
				if os.path.isfile(image_path):
					os.remove(image_path)
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		#count num of posts with the same imageURL
		serializer = PostSerializer(post)
		url_of_element = serializer.data['imageURL']
		elements_num = Post.objects.filter(imageURL=url_of_element).count()
		if elements_num == 1:
			image_file_name = url_of_element.split('/')[-1]
			image_path = os.getcwd() + '\\JBapi\\image_files\\' + image_file_name
			if os.path.isfile(image_path):
				os.remove(image_path)
		post.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	elif request.method == 'PATCH':
		serializer = PostSerializer(post, data=request.data, partial=True)

		if serializer.is_valid():
			if 'imageURL' in request.data:
				#Redownloading image on server in path ".../JBtest/JBapi/image_files"
				load_img_status = load_img(request.data['imageURL'], Response)
				if load_img_status != None:
					return load_img_status
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



### Responsing binary image from URL like "http://localhost:8000/api/posts/96/image". pk - id in database.
### Images located on server, path - ".../JBtest/JB/JBapi/image_files"
@api_view(['GET'])
def get_image(request, pk):
	try:
		post = Post.objects.get(pk=pk)
	except Post.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	serializer = PostSerializer(post)
	path_to_image = os.getcwd() + '\\JBapi\\image_files\\' + serializer.data['imageURL'].split('/')[-1]
	if not os.path.isfile(path_to_image):
		return Response('No image on server, but element in db exists!', status=status.HTTP_404_NOT_FOUND)
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