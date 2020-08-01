from django.contrib import admin
from webapp.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email', 'status', 'created_at')
    list_filter = ('status', )
    search_fields = ('name',)


admin.site.register(Book, BookAdmin)
