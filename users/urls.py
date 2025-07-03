from .views import RegistreView, GetTokenView
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', RegistreView.as_view(), name='register-view'),
    path('get-token/', GetTokenView.as_view(), name='get-token'),


]