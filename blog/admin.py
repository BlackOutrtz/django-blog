from typing import Any
from django.contrib import admin
from blog.models import Category, Sobre, Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug',
    list_display_links = 'name',
    search_fields = 'id', 'name', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('name',)
    }



@admin.register(Sobre)
class SobreAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = 'id', 'title',
    list_display_links = 'title',
    search_fields = 'id', 'title', 'content',
    list_per_page = 50
    ordering = '-id',

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = 'id', 'title', 'is_published', 'created_at', 'category',
    list_display_links = 'title',
    search_fields = 'id', 'slug', 'title', 'content', 'excerpt', 'cover',
    list_per_page = 50
    list_filter = 'is_published', 'category',
    list_editable = 'is_published',
    ordering = '-id',
    readonly_fields = 'created_at', 'updated_at', 
    prepopulated_fields = {
        "slug": ('title',),
    }


