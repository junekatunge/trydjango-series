from django.contrib import admin

# Register your models here.
from .models import Articles

class ArticleAdmin(admin.ModelAdmin):#to make the admin site user friendly
    list_display = ['id','title']
    search_fields = ['title','content']


admin.site.register(Articles, ArticleAdmin)