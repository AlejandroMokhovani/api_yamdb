from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AdminViewSet, UserViewSet
from reviews.views import CategoryViewSet, GenreViewSet, TitleViewSet

router = DefaultRouter()

router.register('users', AdminViewSet, basename='users')
# router.register('users/me/', UserViewSet)
router.register('categories/', CategoryViewSet, basename='categories')
router.register('genres/', GenreViewSet, basename='genres')
router.register('titles/', TitleViewSet, basename='titles')

urlpatterns = [
    path('v1/', include(router.urls)),
  #  path('v1/auth/signup/'),
    path('v1/auth/token/',
    TokenObtainPairView.as_view(),
    name='token_obtain_pair'),
]
