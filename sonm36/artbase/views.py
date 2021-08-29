from django.shortcuts import render, redirect
from django.views import generic

from .forms import ArtistFormSet
from .models import Artist


def add_artists(request):
    if request.method == 'POST':
        formset = ArtistFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                inf = dict()
                inf['name'] = form.cleaned_data.get('name')
                inf['band'] = form.cleaned_data.get('band')
                inf['genre'] = form.cleaned_data.get('genre')
                if inf:
                    artist = Artist.objects.create(info=inf)
                    artist.save()
            return redirect('artbase:show')
    else:
        formset = ArtistFormSet()
    return render(request, 'artbase/index.html', {"formset": formset})


class ArtistsListView(generic.ListView):
    template_name = 'artbase/artists_list.html'
    context_object_name = 'artists'
    model = Artist

    def get_queryset(self):
        return Artist.objects.all()
