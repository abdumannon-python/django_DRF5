from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import authenticate
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
import time

class RegisterView(APIView):
    def post(self,request):
        serializer =RegisterSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        response={
            'status':status.HTTP_200_OK,
            'message':"Siz ro'yxatdan o'tdingiz",
            'data':user.username
        }
        return Response(response)


class Login(APIView):
    def post(self,request):
        username=self.request.data.get('username')
        password=self.request.data.get('password')

        user=authenticate(username=username,password=password)

        if not user:
            return Response({'error':'Parol yoki username xato'})
        refresh_token=RefreshToken.for_user(user=user)

        response={
            'status':status.HTTP_200_OK,
            'message':'login qildiz',
            'refresh_token':str(refresh_token),
            'access':str(refresh_token.access_token)
        }
        return Response(response)
class ProfilUpdate(APIView):
    permission_classes = (IsAuthenticated, )
    def post(self,request):
        serializer=ProfilSerializers(data=request.user)
        username=self.request.data.get('username')
        first_name=self.request.data.get('first_name')
        last_name=self.request.data.get('last_name')

        users=User.objects.filter(username=username).exclude()

        if not users.filter(username=username).exists():
            raise ValidationError({'message':'username mavjud'})

        user=request.user
        serializer.is_valid(raise_exception=True)
        user.username=username
        user.last_name=last_name
        user.first_name=first_name
        user.save()
        return Response({
            "message": "Profil muvaffaqiyatli yangilandi",
            "data": serializer.data
        }, status=status.HTTP_200_OK)




