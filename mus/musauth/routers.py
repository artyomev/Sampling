from rest_framework import routers

from musauth.views import UserViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)