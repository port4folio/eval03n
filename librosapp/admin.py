from django.contrib import admin
from .models import Libro

admin.site.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion', 'isbn')
    search_fields = ('titulo', 'autor')
    list_filter = ('fecha_publicacion',)

# Register your models here.
