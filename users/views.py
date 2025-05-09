from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "تم إنشاء المستخدم"}, status=201)
        return Response(serializer.errors, status=400)
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response({'token': str(refresh.access_token)}, status=200)
        return Response(serializer.errors, status=401)
class ProfileView(APIView):
    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)
    
def register_page(request):
    return render(request, 'Templates/register.html')

def login_page(request):
    return render(request, 'Templates/login.html')

def profile_page(request):
    return render(request, 'Templates/profile.html')


