from rest_framework import serializers
from content.models import Content

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ("text","created_at","private")