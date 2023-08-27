from django.contrib import admin
from .models import Topic

class TopicAdmin(admin.ModelAdmin):
    list_display = ["id", "comment" , "dt"]
    
admin.site.register(Topic,TopicAdmin)