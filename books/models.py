from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(null=False)
    author = models.TextField(null=False)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)
    page_count = models.IntegerField(null=True, blank=True)
    cover = models.URLField(null=True, blank=True)
    language = models.CharField(max_length=30, null=True, blank=True)

    def _str_(self):
        return self.title