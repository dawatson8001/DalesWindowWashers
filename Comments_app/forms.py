from django import forms
from .models import Post


class CommentPostForm(forms.ModelForm):

    content = forms.CharField()

    class Meta:
        model = Post
        fields = ('content',)