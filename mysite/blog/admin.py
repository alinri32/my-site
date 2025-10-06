from django.contrib import admin
from blog.models import *

# Register your models here.
@admin.register(post)
class postadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    exclude = ["counted_view"]
    list_display = ('title' ,'author','status', 'counted_view' , 'created_date' , 'updated_date' , 'published_date')
    list_filter = ('status' ,'author')
    search_fields = ['title' , 'content']

@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)