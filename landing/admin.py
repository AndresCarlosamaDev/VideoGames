from django.contrib import admin
from .models import  Usuario,JuegoPopular,JuegoJugador

# Register your models here.
admin.site.register(Usuario)
admin.site.register(JuegoPopular)
admin.site.register(JuegoJugador)