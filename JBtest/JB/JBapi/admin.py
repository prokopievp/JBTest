from django.contrib import admin
from django import forms
from .serializers import PostSerializer
from .models import Post                                                                                                                             
from .validators import url_validator
import os



###Form for creating elements on admin panel.
class AdminForm(forms.ModelForm):
	title = forms.CharField(max_length = 255)
	text = forms.CharField(widget=forms.Textarea)
	imageURL = forms.CharField(validators=[url_validator])

	
	def __init__(self, *args, **kwargs): 
		super(forms.ModelForm, self).__init__(*args, **kwargs)
		self.fields['title'].label = 'Title'
		self.fields['imageURL'].label = 'Image URL'
		self.fields['text'].label = 'Description'

	def __str__(self):
		return self.title


	
class PostAdmin(admin.ModelAdmin):
	form = AdminForm
	list_display = ['display_title', "text_40", 'updated_at', 'created_at']

	search_fields = ['title']
	search_help_text = 'Search by the title'

	def text_40(self, obj):
		if len(obj.text) <= 40:
			return obj.text
		else:
			return obj.text[:40] + '\n...'
	text_40.short_description = 'Description'
	text_40.admin_order_field = 'text'


	actions = ['delete_model']

	def delete_model(self, request, queryset):
		for post in queryset.iterator():
			serializer = PostSerializer(post)
			url_of_element = serializer.data['imageURL']
			elements_num = Post.objects.filter(imageURL=url_of_element).count()
			if elements_num == 1:
				image_file_name = url_of_element.split('/')[-1]
				image_path = os.getcwd() + '\\JBapi\\image_files\\' + image_file_name
				if os.path.isfile(image_path):
					os.remove(image_path)
			post.delete()
			delete_model.short_description('Delete selected posts')
	

admin.site.disable_action('delete_selected')
admin.site.register(Post, PostAdmin)
