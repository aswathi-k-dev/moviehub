from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import permissions,authentication
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

from films.serializers import UserSerializer
from films.serializers import MovieSerializer
from films.models import Movie

# Create your views here.

class SignUpView(APIView):

    def post(self, request):

        form_data = request.data

        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            instance = User.objects.create_user(**cleaned_data)

            serializer_instance = UserSerializer(instance)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)


class MovieListView(ListAPIView):

    authentication_classes = [ authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

class MovieCreateView(CreateAPIView):
    authentication_classes = [ authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

class MovieRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes = [ authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()



