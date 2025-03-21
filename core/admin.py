from django.contrib import admin

from .models import Book, Borrow, Return


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'pub_date', 'available_copies')
    search_fields = ('title', 'authors')
    list_filter = ('pub_date',)
    ordering = ('-pub_date',)
    date_hierarchy = 'pub_date'


@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrow_date', 'return_date', 'returned')
    search_fields = ('user__username', 'book__title')
    list_filter = ('borrow_date', 'return_date', 'returned')
    list_editable = ('returned',)
    ordering = ('-borrow_date',)


@admin.register(Return)
class ReturnAdmin(admin.ModelAdmin):
    list_display = ('borrow', 'return_date')
    search_fields = ('borrow__user__username', 'borrow__book__title')
    list_filter = ('return_date',)
    ordering = ('-return_date',)
    date_hierarchy = 'return_date'
