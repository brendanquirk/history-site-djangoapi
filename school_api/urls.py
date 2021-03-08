from django.urls import path
from . import views

urlpatterns = [
    path('api/content', views.ContentList.as_view(), name='content_list'),
    path('api/content/<int:pk>', views.ContentDetail.as_view(), name='content_detail'),
    path('api/videos', views.VideoList.as_view(), name='video_list'),
    path('api/study', views.StudyList.as_view(), name='study_list'),
    path('api/tags', views.TagList.as_view(), name='tag_list'),
]
