from rest_framework.routers import DefaultRouter

from ..views.rest import NewsViewSet

router = DefaultRouter()
router.trailing_slash = '/?'

router.register(r'news', NewsViewSet)
