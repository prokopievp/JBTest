import os
from .models import Post  
from .serializers import PostSerializer

def model_del(post):
	serializer = PostSerializer(post)
	url_of_element = serializer.data['imageURL']
	elements_num = Post.objects.filter(imageURL=url_of_element).count()
	if elements_num == 1:
		image_file_name = url_of_element.split('/')[-1]
		image_path = os.getcwd() + '\\JBapi\\image_files\\' + image_file_name
		if os.path.isfile(image_path):
			os.remove(image_path)
	post.delete()