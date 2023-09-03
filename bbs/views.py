from django.shortcuts import render,redirect
from django.views import View

from .models import Category,Topic,PhotoList,DocumentList
from .forms import TopicForm,PhotoForm,DocumentForm

from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator 

import magic

# トップページ
class IndexView(View):
    def get(self, request, *args, **kwargs):
        
        return render(request, "bbs/index.html")

index = IndexView.as_view()

#投稿用ページ
class BbsView(View):

    def get(self, request, *args, **kwargs):
        
        # messages.add_message(request, messages.INFO, "こんにちは")
        # 簡略化↓
        # message.info(request, "こんにちは")
        
        #Topicモデルからオブジェクトをすべ手取得する
        context = {}
        query = Q()
        
        context["categories"] = Category.objects.all()
        
        #キーワード検索
        if "search" in request.GET:
            raw_words = request.GET["search"].replace("　"," ").split()
            words = [w for w in raw_words if w!= ""]
            
            for w in words:
                # AND検索
                query &= Q(comment__icontains=w)
                # OR検索
                query |= Q(comment__icontains=w)
        
        # カテゴリによる検索がある場合
        # id順に並び変え
        topics = Topic.objects.filter(query).order_by("id")
        
        # ページネーションの実装
        paginator = Paginator(topics,1)
        
        if "page" in request.GET:
            context["topics"] = paginator.get_page(request.GET["page"])
        else:
            context["topics"] = paginator.get_page(1)
                    
        return render(request,"bbs/bbs.html",context)

    def post(self, request, *args, **kwargs):
        '''
        posted  = Topic( comment = request.POST["comment"] )
        posted.save()
        print(request.POST["comment"])
        '''
        form = TopicForm(request.POST)
        
        if not form.is_valid():
            #バリデーションNGの理由を表示
            print("バリデーションNG")
            errors = form.errors
            print(errors)
            print(form.errors.get_json_data())
            
            #json形式のデータから辞書（messageとコード）を取得する     
            values = form.errors.get_json_data().values()
            
            ##############################################################################
            #なぜ2重for文で取り出しを行っているのか？->valueが複数の値になることはあり得るのか?#
            #->dict_baluesはセット型のため、subscribeできないことから                       #
            ##############################################################################
            print(type(values))
            for value in values:
                print("valueを表示します")
                print(value)
                for v in value:
                    messages.error(request, v["message"])

            # dict_baluesはセット型のため、subscribeできないことに注意
            #messages.error(values["comment"]["message"])
        else:
            #保存する
            form.save()
            messages.info(request, "投稿内容を保存しました") 
        return redirect("bbs:bbs")

bbs = BbsView.as_view()

# 個別ページ
class SingleView(View):
    def get(self, request, pk, *args, **kwargs):
        context = {}
        
        # pkを使って個別ページに表示するTopicを特定する
        context["topic"] = Topic.objects.filter(id=pk).first()
        
        return render(request, "bbs/single.html", context)

single = SingleView.as_view()


# 削除・編集用ビュー
class BbsDeleteView(View):
    def post(self, request, pk, *args, **kwargs):
        topic = Topic.objects.filter(id=pk).first()
        topic.delete()
        
        # 削除完了のメッセージを表示する 
        messages.info(request, "コメントを削除しました。")
        
        return redirect("bbs:bbs")

class BbsEditView(View):
    def get(self, request, pk, *args, **kwargs):
        context = {}
        context["topic"] = Topic.objects.filter(id=pk).first()
        
        return render(request,"bbs/edit.html", context) 
        
    def post(self, request, pk, *args, **keargs):
        
        topic = Topic.objects.filter(id=pk).first()
        
        form = TopicForm(request.POST,instance=topic)
        
        if not form.is_valid():
            print(form.errors)
            
        form.save()
        messages.info(request,"投稿を編集しました。")
        
        return redirect("bbs:bbs")

    
delete = BbsDeleteView.as_view()
edit = BbsEditView.as_view()

# 画像・pdfファイルのアップロード

ALLOWED_MIME = ["application/pdf"]

class AlbumView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        context["albums"] = PhotoList.objects.all()
        
        return render(request, "bbs/album.html", context)
    
    def post(self, request, *args, **keargs):
        form = PhotoForm(request.POST, request.FILES)

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
            return redirect("bbs:album")
            
        print("バリデーションOK")
        form.save() 
        
        return redirect("bbs:album")     

class DocumentView(View):

    def get(self, request, *args, **kwargs):

        context                 = {}
        context["documents"]    = DocumentList.objects.all()

        return render(request,"bbs/document.html",context)

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
            return redirect("bbs:document")

        mime_type   = magic.from_buffer(request.FILES["file"].read(1024) , mime=True)
        
        if not mime_type in ALLOWED_MIME:
            print("このファイGルのMIMEは許可されていません。")
            print(mime_type)
            messages.error(request, "このファイルのMIMEは許可されていません")
            return redirect("bbs:document")


        print("バリデーションOK")
        form.save()

        return redirect("bbs:document")

album = AlbumView.as_view()
document = DocumentView.as_view()

class CalendarView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "bbs/calendar.html")

calendar = CalendarView.as_view()