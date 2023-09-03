from django.contrib import admin
from .models import Category,Topic,PhotoList,DocumentList

class TopicAdmin(admin.ModelAdmin):
    list_display = ["id", "comment" , "dt"]
    
class PhotoListAdmin(admin.ModelAdmin):
    #指定したフィールドを表示、編集ができる
    list_display        = [ "id","name","age","comment","dt","format_photo" ]
    #list_editable       = [ "name","age","comment","dt" ]


    #指定したフィールドの検索と絞り込みができる
    search_fields       = [ "name","age","comment" ]
    list_filter         = [ "name", "age" , "comment" ]

    #1ページ当たりに表示する件数、全件表示を許容する最大件数(ローカルでも5000件を超えた辺りから遅くなるので、10000~50000辺りが無難)
    list_per_page       = 10
    list_max_show_all   = 20000

    #日付ごとに絞り込む、ドリルナビゲーションの設置
    date_hierarchy      = "dt"

    #画像のフィールドはimgタグで画像そのものを表示させる
    def format_photo(self,obj):
        if obj.photo:
            return format_html('<img src="{}" alt="画像" style="width:15rem">', obj.photo.url)

    #画像を表示するときのラベル(photoのverbose_nameをそのまま参照している)
    format_photo.short_description      = PhotoList.photo.field.verbose_name
    format_photo.empty_value_display    = "画像なし"

admin.site.register(PhotoList,PhotoListAdmin)
admin.site.register(DocumentList)
admin.site.register(Topic,TopicAdmin)
admin.site.register(Category)
