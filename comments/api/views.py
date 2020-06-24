from rest_framework import viewsets
from .serializers import CommentSerializer

from comments.models import Comment
from .permissions import IsGetOrIsAdmin

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    permission_classes = (IsGetOrIsAdmin,)