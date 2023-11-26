from django.contrib import admin

# Register your models here.

from control_blog.models import Usuario, Etiqueta, Entrada

admin.site.register(Usuario)
admin.site.register(Etiqueta)
admin.site.register(Entrada)
