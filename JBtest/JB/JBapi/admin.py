from django.contrib import admin
from django import forms
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
		self.fields['title'].label = 'Название'
		self.fields['imageURL'].label = 'Ссылка на картинку'
		self.fields['text'].label = 'Описание'

	def __str__(self):
		return self.title


	
class PostAdmin(admin.ModelAdmin):
	form = AdminForm
	list_display = ['display_title', "text_40", 'updated_at', 'created_at']

	search_fields = ['title']
	search_help_text = 'Поиск по названию'

	def text_40(self, obj):
		if len(obj.text) <= 40:
			return obj.text
		else:
			return obj.text[:40] + '\n...'
	text_40.short_description = 'Описание'
	text_40.admin_order_field = 'text'
	


admin.site.register(Post, PostAdmin)
