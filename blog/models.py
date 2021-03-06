from django.db import models
from numpy import True_

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=100)   #ブログのタイトル：文字列の入力
  content = models.TextField()   #ブログ記事の内容：テキストの入力
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  is_published = models.BooleanField(default=False) #False=非公開
  image = models.ImageField(upload_to="uploads/", null=True, blank=True)
  
  def __str__(self):
    return self.title