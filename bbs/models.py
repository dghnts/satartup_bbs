from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

import os

# 入力不可な単語を指定する
bad_words = ["あああ", "いいい", "バカ"]

def validate_bad_words(value):
    for word in bad_words:
        if word in value:
            raise ValidationError("不適切な単語が含まれています。", params={'value': value},)
        
class Category(models.Model):
    name = models.CharField(verbose_name="カテゴリ名",max_length=20)
    
    def __str__(self):
        return self.name   

class Topic(models.Model):
    category = models.ForeignKey(Category, verbose_name="カテゴリ", on_delete=models.CASCADE)
    comment = models.CharField(verbose_name="コメント",max_length=2000, validators=[validate_bad_words])
    # 投稿日時を表示する。default値を設定すると，既存のデータには現在の時刻が指定される。これ以降の投稿は投稿日時が設定される
    # defaultを設定しないとエラーが発生
    # 対処法
    # 1.その場限りのdefault値を設定する
    # 2.migarationを中断してdefault値を設定する
    
    dt = models.DateTimeField(verbose_name="投稿日時", auto_now=True)

    name = models.CharField(verbose_name="名前", max_length=20)
    
    def __str__(self):
        return self.comment

class PhotoList(models.Model):
     
     photo = models.ImageField(verbose_name="フォト", upload_to="bbs/album/photo/", blank=True)
     dt = models.DateTimeField(verbose_name="投稿日", default=timezone.now)
     comment = models.CharField(verbose_name="コメント", max_length=2000)
     name = models.CharField(verbose_name="名前", max_length=20, default="匿名希望")
     age = models.IntegerField(verbose_name="年齢", default=20)

class DocumentList(models.Model):
     file = models.FileField(verbose_name="ファイル", upload_to="bbs/document/file/",blank=True)
     
     def file_name(self):
          return os.path.basename(self.file.name)
