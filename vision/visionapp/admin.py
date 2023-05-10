
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Reads, ReadGenre, language, QuizQuestion
# Register your models here.

# admin.site.register(Read)
admin.site.unregister(Group)



class ReadsAdmin(admin.ModelAdmin):
     list_display = ['name']
admin.site.register(Reads, ReadsAdmin)

class ReadGenreAdmin(admin.ModelAdmin):
     list_display = ['genre']
admin.site.register(ReadGenre, ReadGenreAdmin)

class languageAdmin(admin.ModelAdmin):
     list_display = ['language']
     # readonly_fields = ['language']
admin.site.register(language, languageAdmin)

class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'choice1', 'choice2', 'choice3', 'correct_answer')

admin.site.register(QuizQuestion, QuizQuestionAdmin)