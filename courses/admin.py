# admin.py

from django.contrib import admin

from .models import AudioFile, Notebook, Section, Video


@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('notebook', 'title')
    search_fields = ('title',)
    list_filter = ('notebook',)

@admin.register(AudioFile)
class AudioFileAdmin(admin.ModelAdmin):
    list_display = ('section', 'file_path', 'duration')
    search_fields = ('file_path',)
    list_filter = ('section',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('section', 'file_path', 'duration')
    search_fields = ('file_path',)
    list_filter = ('section',)
