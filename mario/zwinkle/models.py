from django.forms import TextInput, Textarea
import datetime
from django.db import models
from django.utils import timezone
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
    gambar = models.FileField(upload_to='images', null=True)
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
status = (
    ('OFF', 'OFF'),
    ('ON', 'ON'),
)

tingkatan_sabuk = (
    ('Putih', 'Putih'),
    ('Kuning', 'Kuning'),
    ('Kuning Strip', 'Kuning Strip'),
    ('Hijau', 'Hijau'),
    ('Hijau Strip', 'Hijau Strip'),
    ('Biru', 'Biru'),
    ('Biru Strip', 'Biru Strip'),
    ('Merah', 'Merah'),
    ('Merah Strip 1', 'Merah Strip 1'),
    ('Merah Strip 2', 'Merah Strip 2'),
)
dojang = (
    ('Krida', 'Krida'),
    ('Bumi Putera', 'Bumi Putera'),
    ('Satria Muda', 'Satria Muda'),
    ('Black Eagle', 'Black Eagle'),
    ('Bangunharjo', 'Bangunharjo'),
)
class krida_model(models.Model):
    krida_model = models.ForeignKey('krida_model_detail', on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=30, verbose_name='Nama')
    ttl = models.CharField(max_length=30)
    dojang = models.CharField(
        max_length=30,
        choices=dojang,
        default='-',
    )
    umur = models.IntegerField()
    waktu = models.CharField(max_length=30)
    sabukawal = models.CharField(
        verbose_name='Dari Sabuk',
        max_length=100,
        choices=tingkatan_sabuk,
        default='Putih',
    )
    sabukujian = models.CharField(
        verbose_name='Ke Sabuk',
        max_length=100,
        choices=tingkatan_sabuk,
        default='Putih',
    )

    hasilujian = models.CharField(
        max_length=100,
        choices=hasil_ujian,
        default='-',
    )

    view = models.CharField(
        max_length=100,
        choices=status,
        default='OFF',
    )

    def __str__(self):
        return "{}.{}".format(self.id,self.umur)

class krida_model_detail(models.Model):
    name = models.CharField(max_length=30, verbose_name='Nama')
    ttl = models.CharField(max_length=30)
    dojang = models.CharField(
        max_length=30,
        choices=dojang,
        default='-',
    )
    umur = models.IntegerField()

    def __str__(self):
        return "{}.{}".format(self.id,self.umur)