from django.urls import include, path
from rest_framework import routers

from .views import UsersViewSet, SingleUserViewSet, create_user, create_token

router = routers.DefaultRouter()

router.register(r'users', UsersViewSet)
router.register('users/me', SingleUserViewSet, basename='me')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', create_user),
    path('v1/auth/token/', create_token),
]
