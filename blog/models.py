# Copyright (c) 2019 Brian Ainsworth. All Rights Reserved.
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    '''
    text boxes for creating a post with author, date, title, and time. 
    '''
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.localdate)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        '''
        action required to publish new post
        '''
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        '''
        creator of given post can authorize comments
        '''
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    '''
    text box for adding comments. gives author, time, and text.
    '''
    post = models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        '''
        final approve command for each comment
        '''
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text



