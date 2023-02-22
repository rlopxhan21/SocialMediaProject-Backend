from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from djoser.views import UserViewSet
from djoser.permissions import CurrentUserOrAdminOrReadOnly
from rest_framework.views import APIView

from .serializers import UpdateProfileImageSerializer, BasicInfoSerializer, AdminInfoSerializer
from .models import User

class ActivateUser(UserViewSet):
    ''' This view is for creating GET request to verify account activation. '''
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())

        kwargs['data'] = {'uid': self.kwargs['uid'], "token": self.kwargs["token"]}

        return serializer_class(*args, **kwargs)
    
    def activation(self, request, *args, **kwargs):
        super().activation(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UpdateProfileImageView(mixins.UpdateModelMixin, generics.GenericAPIView):
    ''' This view is for updating profile image. '''
    serializer_class = UpdateProfileImageSerializer
    queryset = User.objects.all()
    permission_classes = [CurrentUserOrAdminOrReadOnly]


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    

class BasicInfoView(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = BasicInfoSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class BasicInfoDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = BasicInfoSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return User.objects.filter(pk=pk)

    def get(self, reqeust, *args, **kwargs):
        return self.retrieve(reqeust, *args, **kwargs)
    
class AdminInfoView(mixins.UpdateModelMixin, generics.GenericAPIView):
    serializer_class = AdminInfoSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return User.objects.filter(pk=pk)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
class BlackListAPIView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')
            token_obj = RefreshToken(refresh_token)
            token_obj.blacklist()

            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)