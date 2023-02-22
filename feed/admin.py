from django.contrib import admin

from .models import Post, Comment, PostLike


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['content', 'imagefield',
                    'author',  'created', 'updated', 'active']
    list_filter = ['active', 'created', 'updated', 'author']
    date_hierarchy = 'updated'
    search_fields = ['content', 'author']
    raw_id_fields = ['author']
    ordering = ['active']


@admin.register(Comment)
class CommentModel(admin.ModelAdmin):
    list_display = ['content', 'imagefield', 'author',
                    'post', 'created', 'updated', 'active']
    date_hierarchy = 'updated'
    search_fields = ['content', 'author', 'post']
    raw_id_fields = ['author',  'post']
    ordering = ['active']


admin.site.register(PostLike)
