from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api.person import views

router = DefaultRouter()

router.register(r'person', views.PersonViewSet, basename='person')
router.register(r'role', views.RoleViewSet, basename='role')

urlpatterns = [
    url(r'^', include(router.urls)),
]
