from django import forms
from .models import Post

class CommentPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('content','author',)