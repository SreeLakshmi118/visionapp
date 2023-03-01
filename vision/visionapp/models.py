from django.db import models

# # Create your models here.
class Reads(models.Model):
    name = models.CharField(max_length=100 ,unique=True)
    author = models.CharField(max_length=100 ,unique=True)
    img = models.ImageField(upload_to='images/' ,unique=True)
    language = models.ForeignKey('language', on_delete=models.CASCADE)
    genre = models.ForeignKey('ReadGenre', on_delete=models.CASCADE)
    audio = models.FileField(upload_to='audio/' ,unique=True)

    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
        
class ReadGenre(models.Model):
    id=models.AutoField(primary_key=True)
    genre = models.CharField(max_length=100)
    gendesc = models.TextField(default='')
    genimg=models.ImageField(upload_to='images/', default='')
    def __str__(self):
        return self.genre
    
class language(models.Model):
    id=models.AutoField(primary_key=True)
    language = models.CharField(max_length=100)
    langdesc = models.TextField(default='')
    langimg=models.ImageField(upload_to='images/', default='')
    
    def __str__(self):
        return self.language