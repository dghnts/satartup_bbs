from django.shortcuts import render,redirect
from django.views import View

from .models import Album,Document
from .forms import AlbumForm,DocumentForm

from django.contrib import messages

import magic

ALLOWED_MIME = ["application/pdf"]
# Create your views here.
class AlbumView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        context["albums"] = Album.objects.all()
        
        return render(request, "upload/album.html", context)
    
    def post(self, request, *args, **keargs):
        form = AlbumForm(request.POST, request.FILES)

        if not form.is_valid():
            print("バリデーションNG")
            #print(form.errors)
            # messageのみを取得する
            values = form.errors.get_json_data().values()
            print(type(values))
            
            for value in values:
                # valuesのリストオブジェクトを取得する
                for v in value:
                    print(v)
                    #messages.add_message(request,messages.ERROR, v["message"])
                    messages.error(request, v["message"])
            return redirect("upload:album")
            
        print("バリデーションOK")
        form.save() 
        
        return redirect("upload:album")     

class DocumentView(View):

    def get(self, request, *args, **kwargs):

        context                 = {}
        context["documents"]    = Document.objects.all()

        return render(request,"upload/document.html",context)

    def post(self, request, *args, **kwargs):

        form        = DocumentForm(request.POST,request.FILES)
        print(form)
        if not form.is_valid():
            print("バリデーションNG")
            print(form.errors)
            values = form.errors.get_json_data().values()
            print(values)
            
            for value in values:
                print(value)
                for v in value:
                    messages.error(request,v["message"])
            
            '''
            context = {}
            context["errors"] = form.errors
            return render(request, "upload/document.html", context) 
            '''
            return redirect("upload:document")

        mime_type   = magic.from_buffer(request.FILES["file"].read(1024) , mime=True)
        
        if not mime_type in ALLOWED_MIME:
            print("このファイルのMIMEは許可されていません。")
            print(mime_type)
            return redirect("upload:document")


        print("バリデーションOK")
        form.save()

        return redirect("upload:document")

album = AlbumView.as_view()
document = DocumentView.as_view()