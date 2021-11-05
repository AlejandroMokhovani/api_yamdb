from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import include, path
from rest_framework import routers

from .views import UsersViewSet, SingleUserViewSet


router = routers.DefaultRouter()

router.register('users', UsersViewSet, basename='users')
router.register('users/me', SingleUserViewSet, basename='me')

urlpatterns = [
    path('v1/', include(router.urls)),
    # path('v1/auth/signup/'),
    # path('v1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
