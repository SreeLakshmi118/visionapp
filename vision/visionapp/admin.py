from django.contrib import admin

from .models import Reads,ReadGenre,language,Question, Answer
# Register your models here.
# admin.site.register(Read)


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


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Choices', {'fields': ['choice1', 'choice2', 'choice3']}),
    ]
    inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
