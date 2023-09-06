from rest_framework import viewsets
from .serializers import VoteSerializer
from .models import Vote

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
