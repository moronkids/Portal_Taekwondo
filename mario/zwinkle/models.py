from django.db import models

# Create your models here.

class konten(models.Model):
    judul = models.CharField(max_length=30)
    isi = models.TextField()

    def __str__(self):
        return "{}".format(self.judul)

class buat_login(models.Model):
    username = models.CharField(max_length=30)
    password = models.TextField()

    def __str__(self):
        return "{}".format(self.username, self.password)