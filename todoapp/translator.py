from modeltranslation.translator import translator, TranslationOptions
from .models import Todo
class TodoTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

translator.register(Todo, TodoTranslationOptions)