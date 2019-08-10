# Copyright (c) 2019 Brian Ainsworth. All Rights Reserved.
from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):
    '''
    allows a user to create a new post with title and author.
    '''

    class Meta:
        model = Post
        fields = ('author','title','text',)

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        }

class CommentForm(forms.ModelForm):
    '''
    allows other users to comment on any given post.
    '''

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
        }