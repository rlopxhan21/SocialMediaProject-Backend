from django.db import models
from django_resized import ResizedImageField

from useraccount.models import User

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class Post(models.Model):
    content = models.TextField(blank=False, null=False)
    imagefield = ResizedImageField(size=[1456, None], blank=True, null=True, upload_to="post_image/")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="postlist_author")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = models.Manager()
    actives = ActiveManager()

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.content[0:100]

class Comment(models.Model):
    content = models.TextField(blank=False, null=False)
    imagefield = ResizedImageField(size=[1456, None], blank=True, null=True, upload_to='comment_image/')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentlist_author")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment_on_post")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = models.Manager()
    actives = ActiveManager()

    class Meta:
        ordering = ['-updated', '-created']


    def __str__(self):
        return self.content[0:100]
    
class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="liked_post")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_author')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return f"{self.author} commented on {self.post}"