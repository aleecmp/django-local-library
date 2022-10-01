from django.contrib import (
    admin,
)  # django.contrib.admin is a module that provides an interface for site administrators to manage content on the site.

from .models import (
    Author,
    Book,
    BookInstance,
    Genre,
    Language,
)  # Import the models from the models.py file

admin.site.register(Genre)  # Register the Genre model with the admin site.
admin.site.register(Language)  # Register the Language model with the admin site.
# admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(BookInstance)


class BooksInline(admin.TabularInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_of_birth", "date_of_death")
    fields = ["first_name", "last_name", ("date_of_birth", "date_of_death")]
    inlines = [BooksInline]


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "display_genre")
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ("book", "status", "borrower", "due_back", "id")
    list_filter = ("status", "due_back")

    fieldsets = (
        (None, {"fields": ("book", "imprint", "id")}),
        ("Availability", {"fields": ("status", "due_back", "borrower")}),
    )
