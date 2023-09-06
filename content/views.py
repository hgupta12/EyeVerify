from rest_framework import viewsets
from content.models import Content
from .serializers import ContentSerializer

# Create your views here.
class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer