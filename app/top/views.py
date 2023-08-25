from django.shortcuts import render
from django.views import View
# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        
        links = [ {"name": "bbs", "link": "http://127.0.0.1:8000/bbs"},
                  {"name": "album", "link": "http://127.0.0.1:8000/upload/album"},
                  {"name": "document", "link": "http://127.0.0.1:8000/upload/document"},
                 ]
        context = {"links":links}
        
        return render(request, "top/index.html", context)
    
index = IndexView.as_view()    