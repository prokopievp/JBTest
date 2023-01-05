from django.db import models
import os
from django.template.defaultfilters import truncatechars


class Post(models.Model):
	title = models.CharField(max_length = 255)
	text = models.TextField()
	imageURL = models.CharField(max_length = 255)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)

	@property
	def text_20(self, obj):
		return truncatechars(self.text, 20)

	def updated_at(obj):
		return obj.createdAt
	updated_at.short_description = 'Дата создания'
	updated_at.admin_order_field = 'updatedAt'

	def created_at(obj):
		return obj.updatedAt
	created_at.short_description = 'Дата последнего обновления'
	created_at.admin_order_field = 'createdAt'

	def display_title(obj):
		return obj.title
	display_title.short_description = 'Название'
	display_title.admin_order_field = 'title'


	def __str__(self):
		return self.title	