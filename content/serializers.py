from rest_framework import serializers
from content.models import Content

class ContentSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)
    class Meta:
        model = Content
        fields = ("id","text","created_at","private","image_url")