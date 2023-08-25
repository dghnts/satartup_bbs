from django.shortcuts import render,redirect
from django.views import View

from .models import Topic
from .forms import TopicForm

from django.contrib import messages

class BbsView(View):

    def get(self, request, *args, **kwargs):
        
        # messages.add_message(request, messages.INFO, "こんにちは")
        # 簡略化↓
        # message.info(request, "こんにちは")
        
        #Topicモデルからオブジェクトをすべ手取得する
        topics  = Topic.objects.all()
        context = { "topics":topics }
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
    
bbs   = BbsView.as_view()
