from django.db import models

from recall import settings


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
