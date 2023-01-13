from django import forms
from django.contrib import admin

from .model_delete import model_del
from .models import Post
from .validators import url_validator


###Form for creating elements on admin panel.
class AdminForm(forms.ModelForm):
    title = forms.CharField(max_length=255)
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

    @admin.action(description='Delete selected posts')
    def delete_model(self, request, model_or_queryset):
        if type(model_or_queryset) == type(Post()):
            post = model_or_queryset
            model_del(post)
        else:
            for post in model_or_queryset.iterator():
                model_del(post)

    actions = ['delete_model']


admin.site.disable_action('delete_selected')
admin.site.register(Post, PostAdmin)
