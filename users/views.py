from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer, MyTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

# view for registering users
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer