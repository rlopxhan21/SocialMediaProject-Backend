from rest_framework import status, serializers, mixins, generics, permissions
from rest_framework.response import Response

from .models import Post, Comment, PostLike
from .permissions import CurrentUserOrAdminOrReadOnly
from .serializers import PostSerializer, CommentSerializer, PostLikeSerializer

class PostView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Post.actives.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PostDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Post.actives.all()
    serializer_class = PostSerializer
    permission_classes = [CurrentUserOrAdminOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)    
    

class CommentView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Comment.actives.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    
class CommentCreateView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def get_queryset(self, *args, **kwargs):
        pk = self.kwargs['pk']
        return Comment.actives.filter(post_id=pk)
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        serializer.save(post_id=pk, author_id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CommentDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Comment.actives.all()
    serializer_class = CommentSerializer
    permission_classes = [CurrentUserOrAdminOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) 
    

class PostLikeView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = PostLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return PostLike.objects.filter(post_id=pk)
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        return serializer.save(post_id=pk, author_id=self.request.user.id)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        pk = self.kwargs['pk']

        if PostLike.objects.filter(author_id=self.request.user.id, post_id=pk).exists():
            ItemToDelete = PostLike.objects.get(author_id=self.request.user.id, post_id=pk)
            ItemToDelete.delete()

            return Response("Like removed!", status=status.HTTP_204_NO_CONTENT)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)