from django.contrib import admin

from .models import Read, ReadGenre
# Register your models here.
# admin.site.register(Read)


class ReadAdmin(admin.ModelAdmin):
     list_display = ['name']
admin.site.register(Read, ReadAdmin)

class ReadGenreAdmin(admin.ModelAdmin):
     list_display = ['genre']
admin.site.register(ReadGenre, ReadGenreAdmin)

# class languageAdmin(admin.ModelAdmin):
#      list_display = ['language']
# admin.site.register(language, languageAdmin)

