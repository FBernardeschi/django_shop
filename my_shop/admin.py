from django.contrib import admin
from .models import Item, Rubric

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'price', 'published', 'rubric')
    list_display_links = ('name', 'content')
    search_fields = ('name', 'content',)

admin.site.register(Item, ItemAdmin)
admin.site.register(Rubric)
