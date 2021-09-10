from django.db import models

# Create your models here.
class akun(models.Model):
	nama = models.TextField()
	username = models.TextField()
	password = models.TextField()
	voted = models.BooleanField()
	def __str__(self):
		return self.nama
class paslon(models.Model):
	nomorurut=models.IntegerField()
	isputra=models.BooleanField()
	namaketua=models.TextField()
	namawakil=models.TextField()
	votecount=models.IntegerField()
	def __str__(self):
		return self.namaketua
class votemasuk(models.Model):
	waktu=models.DateTimeField()
	pilihan=models.TextField()
	nama=models.TextField()
	def __str__(self):
		return self.nama

