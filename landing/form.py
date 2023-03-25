from django.forms import ModelForm
from .models import JuegoJugador

class JuegoJugadorForm(ModelForm):
    class Meta:
        model = JuegoJugador
        fields = ['nombreJuego','desarrollador', 'estreno', 'genero']