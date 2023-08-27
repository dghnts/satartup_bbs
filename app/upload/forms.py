from django import forms
from .models import PhotoList,DocumentList

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