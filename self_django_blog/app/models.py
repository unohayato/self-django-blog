from django.db import models

# Create your models

class Post(models.Model):
  title = models.CharField(verbose_name="タイトル",max_length=255, blank=False)
  content = models.TextField(verbose_name="投稿内容",blank=False)
  created_at = models.DateTimeField(verbose_name="作成日時",auto_now_add=True)
  updated_at = models.DateTimeField(verbose_name="変更日時",auto_now=True)
  