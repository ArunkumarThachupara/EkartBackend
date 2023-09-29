from django.db import models

class BtsFashion(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='btsfashion/')

class BtsAlbum(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='btsalbums/')

class BT21(models.Model):
    character_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='bt21/')

