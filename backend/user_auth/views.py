# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from django.contrib.auth.models import User

class UserRegisterView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Manually generate JWT tokens
            # install PyJWT==1.7.0
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token

            # Include tokens in the response
            response_data = {
                'user': serializer.data,
                'refresh_token': str(refresh),
                'access_token': str(access_token),
            }

            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
