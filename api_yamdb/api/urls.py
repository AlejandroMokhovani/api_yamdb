from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from rest_framework import routers

from reviews.views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                           ReviewViewSet, TitleViewSet)
from .views import UsersViewSet, SingleUserViewSet, create_user, create_token

router = DefaultRouter()

router.register(r'users', UsersViewSet)
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')
router.register('titles', TitleViewSet, basename='titles')
# + urls comments, reviews
router.register('comments', CommentViewSet, basename='comments')
router.register('reviews', ReviewViewSet, basename='reviews')

urlpatterns = [
    path('v1/', include(router.urls)),
  #  path('v1/auth/signup/'),
    path('v1/auth/signup/', create_user),
    path('v1/auth/token/', create_token),
]
