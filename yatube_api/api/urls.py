from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentsViewSet, FollowViewSet, GroupsViewSet, PostViewSet

router_v1 = DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='posts')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments', CommentsViewSet, basename='comments')
router_v1.register(r'groups', GroupsViewSet, basename='groups')
router_v1.register(r'follow', FollowViewSet, basename='follows')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
