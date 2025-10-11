from django.contrib import admin
from website.models import contact , newsletter

# Register your models here.

@admin.register(contact)
class contactadmin(admin.ModelAdmin):
    list_display = ('name','email','created_date')
    list_filter = ('email',)
    search_fields = ('name','message')

@admin.register(newsletter)
class newsletteradmin(admin.ModelAdmin):
    list_display = ('email',)