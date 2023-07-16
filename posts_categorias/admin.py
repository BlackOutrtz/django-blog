from django.contrib import admin
from posts_categorias.models import Mundo, Politica, PopArtes, Economia, Tecnologia, Educacao, Saude
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Mundo)
class MundoAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = 'id', 'title', 'is_published', 'created_at', 'updated_at', 'category',
    list_display_links = 'title',
    search_fields = 'id', 'slug', 'title', 'content', 'excerpt', 'cover',
    list_per_page = 50
    list_filter = 'is_published', 'category',
    list_editable = 'is_published',
    ordering = '-id',


@admin.register(Politica)
class PoliticaAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = 'id', 'title', 'is_published', 'created_at', 'updated_at', 'category',
    list_display_links = 'title',
    search_fields = 'id', 'slug', 'title', 'content', 'excerpt', 'cover',
    list_per_page = 50
    list_filter = 'is_published', 'category',
    list_editable = 'is_published',
    ordering = '-id',


@admin.register(PopArtes)
class PopArtesAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = 'id', 'title', 'is_published', 'created_at', 'updated_at', 'category',
    list_display_links = 'title',
    search_fields = 'id', 'slug', 'title', 'content', 'excerpt', 'cover',
    list_per_page = 50
    list_filter = 'is_published', 'category',
    list_editable = 'is_published',
    ordering = '-id',


@admin.register(Economia)
class EconomiaAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = 'id', 'title', 'is_published', 'created_at', 'updated_at', 'category',
    list_display_links = 'title',
    search_fields = 'id', 'slug', 'title', 'content', 'excerpt', 'cover',
    list_per_page = 50
    list_filter = 'is_published', 'category',
    list_editable = 'is_published',
    ordering = '-id',


@admin.register(Tecnologia)
class TecnologiaAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = 'id', 'title', 'is_published', 'created_at', 'updated_at', 'category',
    list_display_links = 'title',
    search_fields = 'id', 'slug', 'title', 'content', 'excerpt', 'cover',
    list_per_page = 50
    list_filter = 'is_published', 'category',
    list_editable = 'is_published',
    ordering = '-id',


@admin.register(Educacao)
class EducacaoAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = 'id', 'title', 'is_published', 'created_at', 'updated_at', 'category',
    list_display_links = 'title',
    search_fields = 'id', 'slug', 'title', 'content', 'excerpt', 'cover',
    list_per_page = 50
    list_filter = 'is_published', 'category',
    list_editable = 'is_published',
    ordering = '-id',


@admin.register(Saude)
class SaudeAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = 'id', 'title', 'is_published', 'created_at', 'updated_at', 'category',
    list_display_links = 'title',
    search_fields = 'id', 'slug', 'title', 'content', 'excerpt', 'cover',
    list_per_page = 50
    list_filter = 'is_published', 'category',
    list_editable = 'is_published',
    ordering = '-id',