from django.contrib import admin

from .models import Reads,ReadGenre,language
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

