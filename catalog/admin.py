from django.contrib import admin
from django.db.models import fields
from .models import Author, Genre, Language, Book, BookInstance
from catalog import models

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
# admin.site.register(BookInstance)

# Define the admin class
class AuthorAdminInline(admin.TabularInline):
    model = Book
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name',
                    'date_of_birth', 'date_of_death')

    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    inlines = [AuthorAdminInline]


# Register the admin class with the associated model
# admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for Book using decorator
class BookInsatnceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BookInsatnceInline]

# Register the Admin classes for BookInstance using decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'status', 'due_back')

    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
