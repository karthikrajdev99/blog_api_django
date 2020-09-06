from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import CommentViewSet

router = DefaultRouter()
router.register(r'comment', CommentViewSet)

urlpatterns = [path(r'', include(router.urls))]