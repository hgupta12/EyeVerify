from rest_framework import viewsets
from content.models import Content
from .serializers import ContentSerializer
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.
class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    parser_classes = (MultiPartParser,FormParser)