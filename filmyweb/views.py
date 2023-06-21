from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Film
from .forms import FilmForm, FilmFormExtra
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def wszystkie_filmy(request):
    wszystkie = Film.objects.all()
    return render(request, 'filmy.html', {'filmy': wszystkie})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm
    return render(request, 'registration/register.html', {'form': form})


@login_required
def nowy_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)
    form_extra = FilmFormExtra(request.POST or None, request.FILES or None)

    if form.is_valid() and form_extra.is_valid():
        film = form.save(commit=False)
        dodatkowe_info = form_extra.save()
        film.dodatkowe = dodatkowe_info
        film.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html', {'form': form, 'form_extra': form_extra, 'czy_nowy': True})



@login_required
def edytuj_film(request, id):
    film_id = get_object_or_404(Film, pk=id) # primary key
    form = FilmForm(request.POST or None, request.FILES or None,
                    instance=film_id)
    form_extra = FilmFormExtra(request.POST or None, request.FILES or None,
                               instance=film_id)

    if form.is_valid() and form_extra.is_valid():
        film = form.save(commit=False)
        dodatkowe_info = form_extra.save()
        film.dodatkowe = dodatkowe_info
        film.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html', {'form': form, 'form_extra': form_extra, 'czy_nowy': False})


@login_required
def usun_film(request, id):
    film = get_object_or_404(Film, pk=id)  # primary key

    if request.method == "POST":
        film.delete()
        return redirect(wszystkie_filmy)

    return render(request, 'potwierdz.html', {'film': film})



