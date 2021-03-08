from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=32)

class Content(models.Model):
    tag = models.ForeignKey(Tag, related_name='tag', null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    body = models.TextField()

    @property
    def tag_name(self):
        return self.tag.name

class Video(models.Model):
    tag = models.ForeignKey(Tag, null=True, on_delete=models.SET_NULL)
    video_url = models.CharField(max_length=500)

class Study(models.Model):
    tag = models.ForeignKey(Tag, null=True, on_delete=models.SET_NULL)
    linked_resource = models.CharField(max_length=500)
