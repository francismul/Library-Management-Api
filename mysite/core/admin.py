from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'published_date')
    search_fields = ('title', 'authors')
    list_filter = ('published_date',)
    ordering = ('-published_date',)
    date_hierarchy = 'published_date'
