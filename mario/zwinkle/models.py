from django.forms import TextInput, Textarea
import datetime
from django.db import models
from django.utils import timezone
from PIL import Image
from gm2m import GM2MField


class TestModel(models.Model):
    name = models.CharField(max_length=200)

    locations = GM2MField()

    def __str__(self):
        return self.name
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


    def __str__(self):
        return "{}".format(self.judul)

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
filter = (
    ('ON', 'ON'),
    ('OFF', 'OFF'),
)
a = (
    ('BELUM UJIAN', 'BELUM UJIAN'),
    ('SUDAH UJIAN', 'SUDAH UJIAN'),
)


class Anggota(models.Model):
    dojang = models.CharField(
        max_length=300,
        choices=dojang,
        default='Krida'
    )
    def __str__(self):
        return str(self.dojang)

class Collection(models.Model):
    anggota = models.ForeignKey(
        Anggota,
        related_name='anggota_uti',
        on_delete=models.CASCADE,
        null=True,
    )
    gambar = models.FileField(upload_to='images', blank=True, null=True)
    id_reg = models.IntegerField(blank=True, null=True)
    nama = models.CharField(max_length=300, blank=True, null=True)
    tempat_lahir = models.CharField(max_length=300, blank=True, null=True)
    tanggal_lahir = models.DateField(default=datetime.date.today)
    # filters = models.CharField(
    #     max_length=300,
    #     choices=filter,
    #     default='OFF',
    # )

    def __str__(self):
        return str(self.nama)

    @property
    def last_log(self):
        return self.has_titles.first()


class Ujian(models.Model):
    collection = models.ForeignKey(Collection, related_name="daftar", on_delete=models.CASCADE, null=True)
    ujian_x = models.CharField(
        choices = a,
        default = "BELUM UJIAN",
        max_length = 300
    )
    def __str__(self):
        return str(self.collection)


class CollectionTitle(models.Model):
    """
    A Class for Collection titles.
    """
    collection = models.ForeignKey(Collection, related_name="has_titles", on_delete=models.CASCADE, null=True)
    ujian = models.ForeignKey(Ujian,
        related_name="ujian", on_delete=models.CASCADE, null=True)
    # anggota = models.ForeignKey(Anggota,
    #     related_name="has_titlesx", on_delete=models.SET_NULL, null=True)
    sabukawal = models.CharField(
        verbose_name='Dari Sabuk',
        max_length=100,
        choices=tingkatan_sabuk,
        # default="Putih",
    )
    sabukujian = models.CharField(
        verbose_name='Ke Sabuk',
        max_length=100,
        choices=tingkatan_sabuk,
        # default="Kuning",
    )

    hasilujian = models.CharField(
        max_length=100,
        choices=hasil_ujian,
        null=True,
    )
    waktu = models.CharField(
        max_length=30,
        # default='19.30',

    )


    def __str__(self):
        return str(self.sabukawal)


    # def __str__(self):
    #     return self.anggota




class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name