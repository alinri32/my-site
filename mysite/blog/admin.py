from django.contrib import admin
from blog.models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
@admin.register(post)
class postadmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    exclude = ["counted_view"]
    list_display = ('title' ,'author','status', 'counted_view' , 'created_date' , 'updated_date' , 'published_date')
    list_filter = ('status' ,'author')
    search_fields = ['title' , 'content']
    summernote_fields = ('content',)

@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)