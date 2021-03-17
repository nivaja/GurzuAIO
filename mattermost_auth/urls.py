from django.urls import path, include
from rest_framework.routers import DefaultRouter

from mattermost_auth import viewsets, views

router = DefaultRouter()
router.register(r'mattermost_auth',viewsets.MattermostViewSet,'mattermost_auth')
urlpatterns = [
    path('', include(router.urls)),
    # path('token',views.token)
]