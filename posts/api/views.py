from rest_framework import viewsets
from .serializers import PostSerializer

from posts.models import Post
from .permissions import IsGetOrIsAdmin

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    permission_classes = (IsGetOrIsAdmin,)
