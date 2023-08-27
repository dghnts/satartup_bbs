from django.db import models
import os
from django.utils import timezone

class PhotoList(models.Model):
     
     photo = models.ImageField(verbose_name="フォト", upload_to="upload/album/photo/", blank=True)
     dt = models.DateTimeField(verbose_name="投稿日", default=timezone.now)
     comment = models.CharField(verbose_name="コメント", max_length=2000)
     name = models.CharField(verbose_name="名前", max_length=20, default="匿名希望")
     age = models.IntegerField(verbose_name="年齢", default=20)

class DocumentList(models.Model):
     file = models.FileField(verbose_name="ファイル", upload_to="upload/document/file/",blank=True)
     
     def file_name(self):
          return os.path.basename(self.file.name)
     
'''
class Album(models.Model):
     photo = models.ImageField(verbose_name="フォト", upload_to = "upload/album/photo/")
     
class Document(models.Model):
    file = models.FileField(verbose_name="ファイル",upload_to="upload/document/file/")
    
    def file_name(self):
         return os.path.basename(self.file.name) 
'''