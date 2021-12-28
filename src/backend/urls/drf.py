
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from backend.views import CustomAuthToken
from django.urls import path, include

avi_view = RedirectView.as_view(url='api/v1/', permanent=True)

router = DefaultRouter()
from backend.views import PingPongViewSet

router.register(r'ping', PingPongViewSet, basename='ping')

from news.urls.rest import router as news_router
router.registry.extend(news_router.registry)

urlpatterns = [
    # path(r'api', avi_view),
    # path('api/v1/', include(router.urls)),
    path('', include(news_router.urls)),
    # todo либо авторизация либо заранее получаем токен и настраиваем чтобы избежать подбора
    path('api-token-auth/', CustomAuthToken.as_view())
]

