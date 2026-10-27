from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, authentication
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView

from films.models import Movie
from music.models import Song
from music.serializers import SongSerializer

# Create your views here.

class SongCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk=None):

        movie_id = pk

        movie_object = Movie.objects.get(id=movie_id)

        form_data = request.data

        serializer_instance = SongSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(movie=movie_object,created_by=request.user)

            return Response(data=serializer_instance.data)

        else:
            return Response(data=serializer_instance.errors)


class SongRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = SongSerializer
    queryset = Song.objects.all()