from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Todo, Logo


class TodoAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'status', 'author', 'created_at')
    list_filter = ('status', )
    search_fields = ('title', 'author__username')


admin.site.register(Todo, TodoAdmin)
admin.site.register(Logo)
