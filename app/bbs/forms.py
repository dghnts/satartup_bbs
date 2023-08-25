from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    
    class Meta:
        model = Topic
        fields = [ "comment" ]
        
        error_messages = {
            'comment' : {
                # code : message
                'max_length' : "コメントの文字数が"+str(Topic.comment.field.max_length) + "文字を超えています。",
                'required' : "コメントを入力してください",
            }
        } 

