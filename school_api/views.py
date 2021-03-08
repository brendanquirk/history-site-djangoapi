from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import ContentSerializer, VideoSerializer, StudySerializer, TagSerializer
from .models import Content, Video, Study, Tag

class ContentList(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ContentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class StudyList(generics.ListCreateAPIView):
    queryset = Study.objects.all()
    serializer_class = StudySerializer

class StudyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Study.objects.all()
    serializer_class = StudySerializer

class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
