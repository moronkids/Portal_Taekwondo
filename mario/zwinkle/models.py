from django.forms import TextInput, Textarea
from django.db import models

# Create your models here.

class konten(models.Model):
    judul = models.CharField(max_length=30)
    isi = models.TextField()
    author = models.CharField(max_length=30, null=True)

    def __str__(self):
        return "{}".format(self.judul)

class buat_login(models.Model):
    username = models.CharField(max_length=30)
    password = models.TextField()

    def __str__(self):
        return "{}".format(self.username, self.password)

from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)

class PostModel(models.Model):
    judul   = models.CharField(max_length=100)
    isi   = models.CharField(max_length=1000)
    kategori   = models.CharField(max_length=100)

    def __str__(self):
        return "{}.{}".format(self.id,self.judul)



