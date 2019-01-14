from django.forms import TextInput, Textarea
from django.db import models
from PIL import Image
# Create your models here.
#----- TEMP FILE IMAGE ----

class foto(models.Model):
    photo = models.ImageField(upload_to='images')


#-------------------------
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

CHOICES = (
    ('Python', 'Python'),
    ('Django', 'Django'),
    ('Django Rest Framework', 'Django Rest Framework'),
)
class PostModel(models.Model):
    judul   = models.CharField(max_length=100)
    penulis   = models.CharField(max_length=100)
    isi   = models.CharField(max_length=1000)
    kategori   = models.CharField(
        max_length=100,
        choices=CHOICES,
        default=1,
    )

    def __str__(self):
        return "{}.{}".format(self.id,self.judul)

hasil_ujian = (
    ('LULUS', 'LULUS'),
    ('TIDAK LULUS', 'TIDAK LULUS'),
    ('-', '-'),
)
nominal = (
    ('150.000', '150.000'),
    ('300.000', '300.000'),
    ('LUNAS', 'LUNAS'),
)
status = (
    ('OFF', 'OFF'),
    ('ON', 'ON'),
)
class krida_model(models.Model):

    name = models.CharField(max_length=30)
    umur = models.IntegerField()
    penguji = models.CharField(max_length=30)
    sabuk = models.CharField(max_length=30)
    hasilujian = models.CharField(
        max_length=100,
        choices=hasil_ujian,
        default=1,
    )
    pembayaran = models.CharField(
        max_length=100,
        choices=nominal,
        default=1,
    )
    view = models.CharField(
        max_length=100,
        choices=status,
        default=1,
    )

    def __str__(self):
        return "{}.{}".format(self.id,self.umur)

