from django import forms
from .models import Topic,PhotoList,DocumentList

class TopicForm(forms.ModelForm):
    
    class Meta:
        model = Topic
        fields = [ "category", "comment"]
        
        error_messages = {
            'category' : {
                'required' : "カテゴリを選択してください",
            },
            'comment' : {
                # code : message
                'max_length' : "コメントの文字数が"+str(Topic.comment.field.max_length) + "文字を超えています。",
                'required' : "コメントを入力してください",
            },
        } 

class PhotoForm(forms.ModelForm):
    class Meta:
        model = PhotoList
        fields = ['photo']

        error_messages = {
            'photo' : {
                'required' : "画像を選択してください",
            }
        }

class DocumentForm(forms.ModelForm):
    class Meta:
        model = DocumentList
        fields = ['file']
        
        error_messages = {
            'file' : {
                'required' : "pdfファイルを選択してください",
            }
        }