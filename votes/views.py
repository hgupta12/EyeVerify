from rest_framework import viewsets
from .serializers import VoteSerializer
from .models import Vote
from common.permissions import IsOwnerOrReadOnly

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsOwnerOrReadOnly]
