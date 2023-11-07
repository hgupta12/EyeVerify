from rest_framework import viewsets
from comments.models import Comment
from .serializers import CommentSerializer
from common.permissions import IsOwnerOrReadOnly

# Create your views here.
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]
