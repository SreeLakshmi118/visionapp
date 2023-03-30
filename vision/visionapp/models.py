from django.db import models

# # Create your models here.
class Reads(models.Model):
    name = models.CharField(max_length=100 ,unique=True)
    author = models.CharField(max_length=100 ,unique=True)
    img = models.ImageField(upload_to='images/' ,unique=True)
    language = models.ForeignKey('language', on_delete=models.CASCADE)
    genre = models.ForeignKey('ReadGenre', on_delete=models.CASCADE)
    audio = models.FileField(upload_to='audio/' ,unique=True ,max_length=500)

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
    
    class Meta:
        default_permissions = ()

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    choice1 = models.CharField(max_length=200,default=True)
    choice2 = models.CharField(max_length=200,default=True)
    choice3 = models.CharField(max_length=200,default=True)
    correct_answer = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.question_text 
   
 
    

  

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)


    def __str__(self):
        return self.answer_text

