from django.forms import ModelForm
from .models import Film, DodatkoweInfo, Ocena

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['tytul', 'opis', 'premiera', 'rok', 'imbd_rating', 'plakat']

class FilmFormExtra(ModelForm):
    class Meta:
        model = DodatkoweInfo
        fields = ['gatunek', 'czas_trwania']

class OcenaForm(ModelForm):
    class Meta:
        model = Ocena
        fields = ['gwiazdki', 'recenzja']


