from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'correct')
    search_fields = ('title', 'meaning', 'sentence')