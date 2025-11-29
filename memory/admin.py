from django.contrib import admin
from memory.models import PublicationLanguage, Author, Book, Authorship


class PublicationLanguageAdmin(admin.ModelAdmin):
    list_display = ('language', 'get_language_display',)


admin.site.register(PublicationLanguage, PublicationLanguageAdmin)


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)


class AuthorshipAdmin(admin.ModelAdmin):
    pass


admin.site.register(Authorship, AuthorshipAdmin)
