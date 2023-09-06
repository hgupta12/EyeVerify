from rest_framework import viewsets
from comments.models import Comment
from .serializers import CommnetSerializer

# Create your views here.
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommnetSerializer
