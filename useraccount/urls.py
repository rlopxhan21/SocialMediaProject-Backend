from django.urls import path

from .views import ActivateUser, UpdateProfileImageView, BasicInfoView, BasicInfoDetailView, AdminInfoView, BlackListAPIView

urlpatterns = [
    path('activate/<uid>/<token>/', ActivateUser.as_view({'get': 'activation'}),name="activation"),
    path('updateimage/<int:pk>/', UpdateProfileImageView.as_view(), name="update_image"),
    path('userinfo/', BasicInfoView.as_view(), name='user_info'),
    path('userinfo/<int:pk>/', BasicInfoDetailView.as_view(), name='userinfo_detail'),
    path('admin/userinfo/<int:pk>/', AdminInfoView.as_view(), name='admin_userinfo_detail'),

    # Blacklisting User Token
    path('token/blacklist/', BlackListAPIView.as_view(), name="token_blacklist")
]