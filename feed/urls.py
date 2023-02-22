from django.urls import path

from .views import PostView, PostDetailView, CommentView, CommentCreateView, CommentDetailView, PostLikeView

app_name= "feed"

urlpatterns = [
    path('post/', PostView.as_view(), name="post_list"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('post/<int:pk>/like/', PostLikeView.as_view(), name="post_like"),

    path('comment/', CommentView.as_view(), name="comment_list"),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name="comment_list"),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name="comment_detail"),
]