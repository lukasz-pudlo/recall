from django.db import models

from recall import settings
from django.contrib.auth.models import User


def get_publication_languages():
    return {lang: lang for lang in settings.PUBLICATION_LANGUAGES}


class PublicationLanguage(models.Model):
    language = models.CharField(
        max_length=50, choices=get_publication_languages)

    def __str__(self):
        return self.language


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, through='Authorship', blank=True)
    publication_date = models.DateField(blank=True, null=True)
    publication_languages = models.ManyToManyField(
        PublicationLanguage,
        related_name="publication_langauges",
        related_query_name="publication_languages"
    )

    def __str__(self):
        return f"{self.title}"


class Authorship(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} - {self.book}"


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    note_text = models.TextField(blank=True)

    def __str__(self):
        if self.user.first_name:
            return f"{self.user.first_name}'s note about {self.book.title}"
        else:
            return f"{self.user}'s note about {self.book.title}"


class NoteCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.ForeignKey(
        Note, on_delete=models.SET_NULL, blank=True, null=True)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE
    )
    notecard_text = models.TextField(blank=True)

    def __str__(self):
        if self.note:
            return f"Note card related to {self.note}"
        else:
            return f"Note card related to {self.book.title}"


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True)
    descrption = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Container(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note_card = models.ForeignKey(NoteCard, on_delete=models.CASCADE)
    categories = models.ManyToManyField(
        Category,
        related_name="categories",
        related_query_name="categories")

    def __str__(self):
        return f"{self.book.title} Container"


class Categorisation(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    container = models.ForeignKey(Container, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category} - {self.container}"
