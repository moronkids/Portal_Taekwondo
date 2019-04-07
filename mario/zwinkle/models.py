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
        return "{}".format(self.kategori)

hasil_ujian = (
    ('LULUS', 'Lulus'),
    ('TIDAK LULUS', 'Tidak Lulus'),
    ('AKAN UJIAN', 'Akan Ujian'),
)
status = (
    ('OFF', 'OFF'),
    ('ON', 'ON'),
)
filter = (
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

class Collection(models.Model):
    gambar = models.FileField(upload_to='images', null=True)
    nama = models.CharField(max_length=300, blank=True)
    ttl = models.CharField(max_length=300, blank=True)
    dojang = models.CharField(
        max_length=300,
        choices=dojang,
        default='-',
    )
    umur = models.IntegerField()
    note = models.TextField(blank=True)

    def __str__(self):
        return str(self.nama)

    @property
    def last_log(self):
        return self.has_titles.first()


class CollectionTitle(models.Model):
    """
    A Class for Collection titles.

    """
    collection = models.ForeignKey(Collection,
        related_name="has_titles", on_delete=models.CASCADE)
    sabukawal = models.CharField(
        verbose_name='Dari Sabuk',
        max_length=100,
        choices=tingkatan_sabuk,
        default=None,
    )
    sabukujian = models.CharField(
        verbose_name='Ke Sabuk',
        max_length=100,
        choices=tingkatan_sabuk,
        default=None,
    )

    hasilujian = models.CharField(
        max_length=100,
        choices=hasil_ujian,
        null=True
    )
    waktu = models.CharField(max_length=30)


    class Meta:
        get_latest_by = "hasilujian"
