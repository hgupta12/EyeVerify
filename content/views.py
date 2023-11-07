from rest_framework import viewsets
from content.models import Content
from .serializers import ContentSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import MethodNotAllowed
from common.permissions import IsOwnerOrReadOnly

# Create your views here.
class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    parser_classes = (MultiPartParser,FormParser)
    permission_classes = [IsOwnerOrReadOnly]

    def update(self,request,*args, **kwargs):
        raise MethodNotAllowed("PUT is not allowed for this resource")
    
    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed("PATCH is not allowed for this resource")
        