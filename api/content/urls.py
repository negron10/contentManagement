from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api.content import views

router = DefaultRouter()

router.register(r'category', views.CategoryViewSet, basename='category')
router.register(r'content', views.ContentViewSet, basename='content')
router.register(r'comment', views.CommentViewSet, basename='comment')
router.register(r'file', views.FileViewSet, basename='file')

urlpatterns = [
    url(r'^', include(router.urls)),
]
