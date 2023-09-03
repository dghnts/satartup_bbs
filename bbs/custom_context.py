def links(request):
    
    links = [   
                {"name": "index", "link": "http://127.0.0.1:8000/"},
                {"name": "bbs", "link": "http://127.0.0.1:8000/bbs"},
                {"name": "album", "link": "http://127.0.0.1:8000/album"},
                {"name": "document", "link": "http://127.0.0.1:8000/document"},
                {"name": "calendar", "link": "http://127.0.0.1:8000/calendar"},
            ]
    context = {"links":links}

    return context