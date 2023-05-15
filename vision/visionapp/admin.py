
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Reads, ReadGenre, language, QuizQuestion
# Register your models here.

# admin.site.register(Read)
admin.site.unregister(Group)



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



from django import forms
from django.contrib import admin
import os

class MyModelAdminForm(forms.ModelForm):
    class Meta:
        # models 
        model = Reads
        fields = '__all__'

    def clean_name(self):
        cleaned_data = super().clean() #permanent
        name = cleaned_data.get('name')#field data
        if Reads.objects.filter(name__iexact=name).exists():
          raise forms.ValidationError('Name already exists.')
        return cleaned_data
    
#     def clean_img(self):
#      cleaned_data = super().clean()
#      img = cleaned_data.get('img')
#      if img:
#         img_file_name = os.path.basename(img)
#         if Reads.objects.filter(img__icontains=img_file_name).exists():
#             raise forms.ValidationError('Image already exists.')
#      return cleaned_data

#     def clean_audio(self):
#      cleaned_data = super().clean()
#      audio = cleaned_data.get('audio')
#      if audio:
#         audio_file_name = os.path.basename(audio)
#         if Reads.objects.filter(audio__icontains=audio_file_name).exists():
#             raise forms.ValidationError('Audio already exists.')
#      return cleaned_data

class ReadsAdmin(admin.ModelAdmin):
     form = MyModelAdminForm
     list_display = ['name']
admin.site.register(Reads, ReadsAdmin)

# class MyModelAdmin(admin.ModelAdmin):
#     form = MyModelAdminForm

# admin.site.register(Reads, MyModelAdmin)