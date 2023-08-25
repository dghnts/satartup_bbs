from django.db import models
from django.core.exceptions import ValidationError

# 入力不可な単語を指定する
bad_words = ["あああ", "いいい", "バカ"]

def validate_bad_words(value):
    for word in bad_words:
        if word in value:
            raise ValidationError("不適切な単語が含まれています。", params={'value': value},)
        
class Topic(models.Model):
    comment = models.CharField(verbose_name="コメント",max_length=2000, validators=[validate_bad_words])

