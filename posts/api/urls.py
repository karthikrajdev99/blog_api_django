from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import PostViewSet

router = DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns = [path(r'', include(router.urls))]