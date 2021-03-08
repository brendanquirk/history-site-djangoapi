from rest_framework import serializers
from .models import Content, Video, Tag, Study

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('id', 'tag_id', 'tag_name', 'title', 'body', )

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'video_url')

class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = ('id', 'linked_resource')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')
